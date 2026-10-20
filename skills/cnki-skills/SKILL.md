---
name: cnki-skills
description: Search and inspect CNKI literature and journals, export citations, and obtain authorized downloads using the installed CNKI skill collection and Chrome DevTools MCP. Use for Chinese literature or CNKI workflows.
---

# cnki-skills

This is a project-scoped entry point for the pinned upstream collection.

1. Search `references/catalog.md` for the requested topic or workflow. It indexes 10 source skills. Read only the matching entries.
2. Open the selected linked `SKILL.md`, resolving its path relative to the catalog file, and follow its instructions. Keep scripts, references, and assets in their original source directory.
3. Check that the tools, network access, or accounts needed by that selected skill are available before claiming the operation works.
4. Source code is installed locally; optional external accounts and services are not provisioned by installing these instructions. Do not execute installers for unrelated packs.

From the repository root, upstream README and license are under `.local/skill-sources/cnki-skills/`. Exact source revisions are recorded in the project-root `skills.lock.json`.

## CNKI runtime

The `chrome-devtools` server is configured in the project `.codex/config.toml`.
Use its browser tools to navigate CNKI and run the selected source skill's scripts.
Downloads can require an institutional subscription or manual sign-in. Pause for user interaction on CAPTCHA; do not bypass access controls.
