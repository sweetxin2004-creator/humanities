# ai-research-skills: 17 indexed skills

Only open the skill matching the current task. Paths are relative to this catalog.

## research-hub
- Skill file: [research-hub](../../../.local/skill-sources/research-hub/skills/research-hub/SKILL.md)
- Operate research-hub workflows for discovery, ingest, organization, NotebookLM, dashboard, and maintenance.

## research-hub-multi-ai
- Skill file: [research-hub-multi-ai](../../../.local/skill-sources/research-hub/skills/research-hub-multi-ai/SKILL.md)
- Router that writes `.coord/multi_ai_plan.md` when a single round will need >=2 delegates (codex-delegate + antigravity-delegate, multiple parallel codex or agy sessions, or mixed handoffs). The router decides task splitting, dependency ordering, and reconciliation; codex-delegate and antigravity-delegate are the supported leaves for bounded mechanical execution while long-context, CJK, judgment, and review work stays primary.

## research-context-compressor
- Skill file: [research-context-compressor](../../../.local/skill-sources/research-hub/skills/research-context-compressor/SKILL.md)
- Create .research manifests so future AI sessions avoid repeated repo scans.

## research-project-orienter
- Skill file: [research-project-orienter](../../../.local/skill-sources/research-hub/skills/research-project-orienter/SKILL.md)
- Read .research manifests and produce a concise orientation memo.

## research-design-helper
- Skill file: [research-design-helper](../../../.local/skill-sources/research-hub/skills/research-design-helper/SKILL.md)
- Guide a researcher through 5 Socratic segments (research question sharpening, expected mechanism, identifiability check, validation plan, risk register) after an explicit human topic choice, and produce .research/design_brief.md. Does NOT write the model spec or invent the research question - guides the human to articulate them.

## literature-triage-matrix
- Skill file: [literature-triage-matrix](../../../.local/skill-sources/research-hub/skills/literature-triage-matrix/SKILL.md)
- Compare papers by method, data, claims, limitations, and relevance.

## paper-memory-builder
- Skill file: [paper-memory-builder](../../../.local/skill-sources/research-hub/skills/paper-memory-builder/SKILL.md)
- Extract .paper claims and figure memory for manuscript work.

## paper-summarize
- Skill file: [paper-summarize](../../../.local/skill-sources/research-hub/skills/paper-summarize/SKILL.md)
- Fill per-paper Key Findings / Methodology / Relevance in both Obsidian markdown and Zotero child notes after `research-hub auto` ingests a cluster.

## notebooklm-brief-verifier
- Skill file: [notebooklm-brief-verifier](../../../.local/skill-sources/research-hub/skills/notebooklm-brief-verifier/SKILL.md)
- Verify NotebookLM briefs against uploaded source bundles.

## gap-to-topic
- Skill file: [gap-to-topic](../../../.local/skill-sources/research-hub/skills/gap-to-topic/SKILL.md)
- Turn a research area into a go/no-go decision dossier for candidate thesis or proposal topics, allowing zero or multiple justified options - a 3-gate verdict (gap open? a contribution? feasible?) with the evidence laid out so the researcher can verify it. Hands the final worth-it call and topic choice back to the researcher and advisor.

## zotero-library-curator
- Skill file: [zotero-library-curator](../../../.local/skill-sources/research-hub/skills/zotero-library-curator/SKILL.md)
- Audit and curate a Zotero library - find duplicate DOIs, orphan items missing required tags, propose collection rebinds, generate tag hygiene reports, emit preview-only cleanup plans. Defers all CRUD to the standalone zotero-skills skill or research-hub zotero CLI.

## research-workflow-orchestrator
- Skill file: [research-workflow-orchestrator](../../../.local/skill-sources/research-hub/skills/research-workflow-orchestrator/SKILL.md)
- Resumable eight-stage HITL controller for orient, scope, discover, synthesize, design, execute, write, and release workflows.

## academic-writing-skills
- Skill file: [academic-writing-skills](../../../.local/skill-sources/academic-writing-skills/skills/academic-writing-skills/SKILL.md)
- Lifecycle-aware outlining, paragraph and section drafting, evidence alignment, prose consistency, cross-artifact revision, and submission release checks.

## paper-review
- Skill file: [paper-review](../../../.local/skill-sources/academic-writing-skills/skills/paper-review/SKILL.md)
- Cross-disciplinary, evidence-safe scientific review with progressively loaded display-provenance, method, domain, round, and optional reviewer modules.

## zotero-skills
- Skill file: [zotero-skills](../../../.local/skill-sources/zotero-skills/skills/zotero-skills/SKILL.md)
- Deep Zotero CRUD, collections, tags, item edits, PDF attachments, and library maintenance.

## codex-delegate
- Skill file: [codex-delegate](../../../.local/skill-sources/codex-delegate/skills/codex-delegate/SKILL.md)
- Minimal synchronous Codex CLI compatibility adapter for bounded mechanical work and existing brief/result/sentinel consumers; the supervisor verifies scope and tests.

## antigravity-delegate
- Skill file: [antigravity-delegate](../../../.local/skill-sources/antigravity-delegate/skills/antigravity-delegate/SKILL.md)
- Leaf delegate restricted to bounded non-honesty-critical mechanical work. Claude supervises; agy CLI executes.
