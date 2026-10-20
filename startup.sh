#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
python3 scripts/install_skills.py --check
"$ROOT/bin/paper-search" sources >/dev/null
"$ROOT/bin/humanities-review" --help >/dev/null
test -f "$ROOT/tools/chrome-devtools/node_modules/chrome-devtools-mcp/build/src/index.js"
printf '%s\n' 'Research skills and local tools are installed.' \
  'Codex discovers the 10 project entries through .agents/skills.' \
  'Restart/open a new Codex session after first installation to refresh its skill catalog.' \
  'CNKI operations require Chrome DevTools MCP and appropriate CNKI access.'
