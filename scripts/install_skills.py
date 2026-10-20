#!/usr/bin/env python3
"""Install pinned research-skill sources and register project-scoped entries."""
import argparse
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / ".local" / "skill-sources"
LOCK = json.loads((ROOT / "skills.lock.json").read_text())


def git(directory, *args):
    return subprocess.check_output(
        ["git", "-C", str(directory), *args], text=True
    ).strip()


def link(path, target, check):
    target = target.resolve()
    if path.is_symlink():
        if path.resolve() != target:
            raise RuntimeError(f"Existing link points elsewhere; preserve and inspect it: {path}")
    elif path.exists():
        raise RuntimeError(f"Refusing to replace existing file: {path}")
    elif check:
        raise RuntimeError(f"Missing skill link: {path}; run bash install.sh")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.symlink_to(os.path.relpath(target, path.parent), target_is_directory=True)
    if not path.exists():
        raise RuntimeError(f"Broken skill link: {path}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Offline integrity check only")
    args = parser.parse_args()
    for source in LOCK["sources"]:
        directory = CACHE / source["id"]
        if not directory.exists():
            if args.check:
                raise RuntimeError(f"Missing source: {source['id']}; run bash install.sh")
            directory.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run([
                "git", "clone", "--quiet", "--no-checkout", "--depth", "1",
                f"https://github.com/{source['repository']}.git", str(directory)
            ], check=True)
            subprocess.run([
                "git", "-C", str(directory), "fetch", "--quiet", "--depth", "1",
                "origin", source["commit"]
            ], check=True)
            subprocess.run([
                "git", "-C", str(directory), "checkout", "--quiet", "--detach", source["commit"]
            ], check=True)
        if git(directory, "rev-parse", "HEAD") != source["commit"]:
            raise RuntimeError(f"Source version mismatch, refusing to reset local work: {directory}")
        if git(directory, "status", "--porcelain=v1", "--untracked-files=no"):
            raise RuntimeError(f"Source has tracked changes; preserve them before refreshing: {directory}")

    aers = CACHE / "Auto-Empirical-Research-Skills"
    if not args.check:
        subprocess.run([
            "git", "-C", str(aers), "submodule", "update", "--init", "--depth", "1"
        ], check=True)
    submodules = git(aers, "submodule", "status")
    if any(line.startswith(("-", "+", "U")) for line in submodules.splitlines()):
        raise RuntimeError("AERS submodule is missing or at the wrong version")

    for entry in LOCK["entries"]:
        directory = ROOT / "skills" / entry["name"]
        if not (directory / "SKILL.md").is_file():
            raise RuntimeError(f"Skill entry has no SKILL.md: {directory}")
        if not entry.get("router"):
            source_skill = CACHE / entry["source"] / entry["path"] / "SKILL.md"
            if not source_skill.is_file():
                raise RuntimeError(f"Missing upstream skill: {source_skill}")
        link(ROOT / ".agents" / "skills" / entry["name"], directory, args.check)
    print(f"Verified {len(LOCK['entries'])} skill entries from {len(LOCK['sources'])} pinned sources.")


if __name__ == "__main__":
    main()
