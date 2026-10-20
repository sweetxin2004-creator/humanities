#!/usr/bin/env python3
"""Verify native skill discovery, local review, and both stdio MCP servers.

Run with .local/skill-sources/paper-search-mcp/.venv/bin/python.
No LLM calls or external academic API requests are made by this check.
"""
import asyncio
import json
import os
from pathlib import Path
import re
import subprocess

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / ".local" / "verification"


async def native_discovery():
    home = STATE / "codex-home"
    home.mkdir(parents=True, exist_ok=True)
    with (STATE / "codex.stderr").open("w") as stderr:
        proc = await asyncio.create_subprocess_exec(
            "codex", "app-server", "--stdio", cwd=ROOT,
            env={**os.environ, "CODEX_HOME": str(home)},
            stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=stderr,
        )

        async def send(message):
            proc.stdin.write((json.dumps(message) + "\n").encode())
            await proc.stdin.drain()

        try:
            await send({"id": 1, "method": "initialize", "params": {
                "clientInfo": {"name": "research_skills_check", "version": "1.0"},
                "capabilities": {"experimentalApi": True},
            }})
            while True:
                line = await asyncio.wait_for(proc.stdout.readline(), 45)
                if not line:
                    raise RuntimeError("Codex app-server ended before skills/list returned")
                message = json.loads(line)
                if message.get("id") == 1:
                    if "error" in message:
                        raise RuntimeError(message["error"])
                    await send({"method": "initialized", "params": {}})
                    await send({"id": 2, "method": "skills/list", "params": {
                        "cwds": [str(ROOT)], "forceReload": True,
                    }})
                if message.get("id") == 2:
                    (STATE / "skills-list.json").write_text(json.dumps(message, indent=2))
                    data = message["result"]["data"][0]
                    assert not data["errors"], data["errors"]
                    skills = [s for s in data["skills"] if s["scope"] == "repo"]
                    expected = {
                        re.search(r"^name: (.+)$", p.read_text(), re.M).group(1)
                        for p in (ROOT / "skills").glob("*/SKILL.md")
                    }
                    assert len(skills) == 10, len(skills)
                    assert {s["name"] for s in skills} == expected
                    assert all(s["enabled"] for s in skills)
                    print("PASS: Codex discovered all 10 project skill entries without parse errors.")
                    break
        finally:
            if proc.returncode is None:
                proc.terminate()
                try:
                    await asyncio.wait_for(proc.wait(), 5)
                except asyncio.TimeoutError:
                    proc.kill()
                    await proc.wait()


async def check_mcp(name, browser=False):
    env = dict(os.environ)
    if browser:
        env["RESEARCH_CHROME_NO_SANDBOX"] = "1"
    params = StdioServerParameters(
        command="bash", args=[str(ROOT / "bin" / name)], cwd=str(ROOT), env=env
    )
    with (STATE / f"{name}.stderr").open("w") as stderr:
        async with stdio_client(params, errlog=stderr) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = (await session.list_tools()).tools
                names = {tool.name for tool in tools}
                if not browser:
                    assert "search_crossref" in names
                    print(f"PASS: paper-search MCP initialized and exposed {len(tools)} tools.")
                else:
                    assert {"new_page", "evaluate_script"} <= names
                    connections = set()

                    async def respond(reader, writer):
                        connections.add(writer)
                        try:
                            await reader.readuntil(b"\r\n\r\n")
                            body = b"<title>Research skills check</title><p id='ready'>ready</p>"
                            writer.write(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: "
                                         + str(len(body)).encode() + b"\r\nConnection: close\r\n\r\n" + body)
                            await writer.drain()
                        except asyncio.IncompleteReadError:
                            pass  # Chromium can open a speculative connection without a request.
                        finally:
                            writer.close()
                            await writer.wait_closed()
                            connections.discard(writer)

                    server = await asyncio.start_server(respond, "127.0.0.1", 0)
                    try:
                        port = server.sockets[0].getsockname()[1]
                        page = await session.call_tool("new_page", {
                            "url": f"http://127.0.0.1:{port}/"
                        })
                        assert not page.isError, page
                        result = await session.call_tool("evaluate_script", {
                            "function": "() => ({title: document.title, status: document.querySelector('#ready').textContent})"
                        })
                    finally:
                        server.close()
                        for writer in tuple(connections):
                            writer.close()
                        await server.wait_closed()
                    assert not result.isError, result
                    content = " ".join(item.text for item in result.content if hasattr(item, "text"))
                    assert "Research skills check" in content and "ready" in content, content
                    print(f"PASS: Chrome DevTools MCP exposed {len(tools)} tools and evaluated a real browser page.")


def check_review():
    result = subprocess.run(
        [str(ROOT / "bin/humanities-review"), "-", "--format", "json"],
        input="显而易见，所有学者都认为人工智能必然改变一切。这证明该理论完全正确。\n",
        capture_output=True, text=True, cwd=ROOT, check=True,
    )
    data = json.loads(result.stdout)
    (STATE / "review.json").write_text(json.dumps(data, indent=2, ensure_ascii=False))
    assert data["warnings"] >= 1 and data["issues"], "Review missed the sample paragraph's overclaims"
    print("PASS: Humanities review processed a paragraph and returned structured JSON.")


async def main():
    STATE.mkdir(parents=True, exist_ok=True)
    await native_discovery()
    check_review()
    await asyncio.wait_for(check_mcp("paper-search-mcp"), 60)
    await asyncio.wait_for(check_mcp("chrome-devtools", browser=True), 60)


if __name__ == "__main__":
    asyncio.run(main())
