# Research skills for this repository

Use the existing checkout. Do not create a Git worktree unless the user requests one.

Ten project-scoped research skill entries are under `.agents/skills/`, pointing
to the small entry files in `skills/`. Match the user's research task to one
entry, read its `SKILL.md`, and then read only the referenced upstream skill.
Do not load the entire catalogs into context. Upstream sources are pinned in
`skills.lock.json` and retained under the ignored `.local/skill-sources/`.

If dependencies or sources are missing, run `bash install.sh` from this
repository. Run `bash startup.sh` to check retained installation state.
Codex sessions opened after installation discover entries automatically;
an already-running conversation may need to read entry files explicitly.

The project `.codex/config.toml` declares paper-search and Chrome DevTools MCP
servers for Codex clients that load trusted project configuration. Cloud chat
tools are managed by the platform and do not change merely because that file
exists. CLI wrappers remain usable as `./bin/paper-search`,
`./bin/humanities-review`, and `./bin/humanities-search`.

Installing skill instructions does not establish live API access, CNKI login,
Zotero connectivity, NotebookLM authentication, R/Stata availability, or model
delegation. Verify the selected operation and report actual access errors.
