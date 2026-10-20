# AcademicForge: 33 indexed skills

Only open the skill matching the current task. Paths are relative to this catalog.

## algorithmic-art
- Skill file: [algorithmic-art](../../../.local/skill-sources/AcademicForge/skills/claude-science/algorithmic-art/SKILL.md)
- Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.

## alphafold2
- Skill file: [alphafold2](../../../.local/skill-sources/AcademicForge/skills/claude-science/alphafold2/SKILL.md)
- Predict protein structure for monomers and multimers with AlphaFold2 via the ColabFold runner (Mirdita et al. 2022, github.com/sokrypton/ColabFold; AlphaFold2 Jumper et al. 2021). Reach for this skill to fold a sequence or complex with the AF2/AF2-Multimer evoformer, to validate designed sequences by self-consistency pLDDT, ipTM, and RMSD, or to run a quick MSA-backed prediction using the public MMseqs2 server.

## boltz
- Skill file: [boltz](../../../.local/skill-sources/AcademicForge/skills/claude-science/boltz/SKILL.md)
- Structure prediction for protein, nucleic-acid, and small-molecule complexes with Boltz-2 (Passaro & Wohlwend et al. 2025, github.com/jwohlwend/boltz). Reach for this skill to validate designed binders against a target, to co-fold a protein with a SMILES or CCD ligand, or to get an open-source AlphaFold3 alternative with optional binding-affinity prediction.

## borzoi
- Skill file: [borzoi](../../../.local/skill-sources/AcademicForge/skills/claude-science/borzoi/SKILL.md)
- Predict genome-wide functional tracks (RNA-seq, CAGE, DNase, ChIP) from DNA sequence with Borzoi. Use this skill when: (1) Scoring the regulatory effect of a variant on expression/accessibility, (2) Generating predicted coverage tracks for a locus, (3) Prioritising non-coding variants by predicted track delta.

## chai1
- Skill file: [chai1](../../../.local/skill-sources/AcademicForge/skills/claude-science/chai1/SKILL.md)
- Structure prediction for protein, nucleic-acid, and small-molecule complexes with the Chai-1 foundation model (Chai Discovery 2024, github.com/chaidiscovery/chai-lab). Reach for this skill to predict an antibody-antigen or protein-ligand complex from a single FASTA, to re-fold designed binders as an AlphaFold-multimer alternative, or to drive co-folding from Python for batched campaigns on a GPU.

## compute-env-setup
- Skill file: [compute-env-setup](../../../.local/skill-sources/AcademicForge/skills/claude-science/compute-env-setup/SKILL.md)
- Set up a compute environment on a remote provider so Claude Science jobs can run there. Covers direct SSH/conda hosts, Slurm clusters, container-via-bridge runners, and managed-API providers (Modal, GCP, RunPod). Use when standing up a new provider, porting an env to a different backend, adding a tool that needs its own software stack, or wiring weight caches. Triggers on "new compute provider", "set up env on", "port env to", "build GPU image", "weight cache", "compute_details", "conda env on the box", "apptainer on slurm".

## customize
- Skill file: [customize](../../../.local/skill-sources/AcademicForge/skills/claude-science/customize/SKILL.md)
- Create, configure, and maintain custom agent profiles and author new skills via the `repl` tool. Use when the user wants to create an agent profile, build a custom agent, modify agent capabilities, attach or detach skills/connectors on a profile, author a skill, or inspect which connectors and tools are available. Also use whenever you need the `host.agents.*` or `host.skills.*` Python SDK.

## diffdock
- Skill file: [diffdock](../../../.local/skill-sources/AcademicForge/skills/claude-science/diffdock/SKILL.md)
- Predict small-molecule binding poses with DiffDock-L (Corso et al. 2023/2024, github.com/gcorso/DiffDock) — blind diffusion docking that places a ligand into a protein pocket without a predefined search box and ranks the samples with a learned confidence model. Reach for this skill to dock a SMILES or SDF against a PDB, to generate ranked 3D poses for a small fragment library, or to get a starting pose for downstream rescoring. DiffDock predicts geometry, not affinity.

## esmfold2
- Skill file: [esmfold2](../../../.local/skill-sources/AcademicForge/skills/claude-science/esmfold2/SKILL.md)
- Biohub ESMFold2 / ESMFold2-Fast all-atom co-folding (Candido et al. 2026, github.com/Biohub/esm). Single-sequence and MSA modes; protein, DNA, RNA, ligand (CCD/SMILES), modified residues. FoldBench Ab-Ag 50-55%, PPI 70-77% DockQ-pass. Also covers the ESMC-{300M,600M,6B} protein language models from the same release: masked-LM logits, hidden states, mutation scoring, contact prediction, and the SAE interpretability head. MIT-licensed weights on HuggingFace org `biohub`. Use this skill when: (1) Predicting complex structures with single-sequence input, (2) Validating designed binders with ESMFold2-Fast, (3) Running ESMFold2 with MSA input, (4) Getting ESMC embeddings or per-residue mutation scores, (5) Choosing kernel backend and sampling-step settings for paper-faithful throughput.

## evo2
- Skill file: [evo2](../../../.local/skill-sources/AcademicForge/skills/claude-science/evo2/SKILL.md)
- Score, embed, and generate DNA sequences with Evo 2, a long-context genomic foundation model. Use this skill when: (1) Computing per-nucleotide or per-sequence likelihoods for variant effect scoring, (2) Embedding genomic windows for downstream classification, (3) Generating DNA conditioned on a prefix, (4) Scoring regulatory or coding regions across species.

## fair-esm2
- Skill file: [fair-esm2](../../../.local/skill-sources/AcademicForge/skills/claude-science/fair-esm2/SKILL.md)
- Embed proteins with Meta AI's ESM-2 (`fair-esm` package). Use this skill when: (1) Extracting per-residue or per-sequence embeddings for downstream ML, (2) Masked-LM likelihood / mutation effect scoring, (3) Contact prediction from a sequence.

## figure-composer
- Skill file: [figure-composer](../../../.local/skill-sources/AcademicForge/skills/claude-science/figure-composer/SKILL.md)
- Compose one publication-grade multi-panel figure. Entry from a one-line claim + data files, OR from an existing figure via `derive_outline_prompt` (you read the PNG). Runs a per-figure loop: outline (12-col grid, per-panel ask + label_budget) → render each panel with `panel_task` (loading `figure-style`), one at a time or parallelized → tile + stamp letters with `compose_figure` → adversarial composite self-review with two-tier feedback (Tier-1 outline_revisions / Tier-2 per-panel violations) → regen affected panels, ≤3 rounds. Helpers: panel_task / compose_figure / compose_crops / composite_review_task / derive_outline_prompt. For one standalone plot use `figure-style`; for whole-paper figure ordering use `paper-narrative`.

## figure-style
- Skill file: [figure-style](../../../.local/skill-sources/AcademicForge/skills/claude-science/figure-style/SKILL.md)
- Publication-grade figure correctness and legibility rules. Load before drawing any plot and call `apply_figure_style()` — sets a role-mapped font-size ladder, outward ticks, frameless legends, and 300-dpi output. The skill is a checklist, not a house look: data fidelity (claim-titles tested against every row, excluded data never enters summaries), label economy (floor and ceiling), colour threading, chart-choice-by-data-shape, layout, and a render-then-verify QA loop (bbox collision + per-panel perceptual check). Ships helpers: focal_palette, bar_with_points, strip_with_median, end_of_line_labels, panel_letter, set_frame, panel_crops. For multi-panel figures load `figure-composer`; for whole-paper figure arc load `paper-narrative`.

## indication-dossier
- Skill file: [indication-dossier](../../../.local/skill-sources/AcademicForge/skills/claude-science/indication-dossier/SKILL.md)
- Generate a therapeutic indication dossier. Covers the patient population, epidemiology, disease biology, standard of care, regulatory precedent, and landmark clinical trials.

## learn
- Skill file: [learn](../../../.local/skill-sources/AcademicForge/skills/claude-science/learn/SKILL.md)
- Use this skill when the user wants intellectual understanding — learning how or why something works, not getting a task done or soliciting Claude's judgment. Trigger for: - Explicit learning requests: teach, explain, ELI5, walk me through, quiz me, flashcards, "I'm rusty on"; definitions ("what is X") - Terse concept names implying "help me understand this": "Galois theory," "transformers, from scratch" - Confusion signals: "won't stick," "keep mixing these up," "not getting it" - Learning-path questions: prerequisites, sequencing, what to study before X - Conceptual questions about mechanisms, causes, or dynamics Don't trigger for: - Tasks: coding, writing, calculation, translation, factual lookup, news updates - Personal troubleshooting; resource/textbook recommendations - Claude's evaluative verdict: opinion prompts ("do you think X", "settle this", "honest take", "is X dead / still taken seriously") and interpretive takes ("was X really as harsh as people say")

## ligandmpnn
- Skill file: [ligandmpnn](../../../.local/skill-sources/AcademicForge/skills/claude-science/ligandmpnn/SKILL.md)
- Inverse-fold a backbone with ligand, nucleic-acid, and metal context using LigandMPNN (Dauparas et al. 2023, github.com/dauparas/LigandMPNN). Reach for this skill to redesign the residues lining a binding pocket around a bound small molecule or cofactor, to design metal-coordinating sites where the geometry must be respected, or to get threaded designed-sequence PDBs out of any MPNN run.

## literature-review
- Skill file: [literature-review](../../../.local/skill-sources/AcademicForge/skills/claude-science/literature-review/SKILL.md)
- Find, verify, and synthesize scientific literature — from "what's the seminal paper for X" through full multi-source reviews. Covers grounding claims in real retrieved sources, avoiding fabricated citations, handling retractions, and calibrating confidence to evidence strength.

## managed-model-endpoints
- Skill file: [managed-model-endpoints](../../../.local/skill-sources/AcademicForge/skills/claude-science/managed-model-endpoints/SKILL.md)
- Register a model service in the managed family — a local model server container the daemon starts/stops on demand, or a remote upstream model API (https). Read the runbook, allocate a port (local only), compose idempotent start/stop scripts (local only), register once. Load when the user wants a model service available for inference, or when list_compute shows managed endpoints.

## openfold3
- Skill file: [openfold3](../../../.local/skill-sources/AcademicForge/skills/claude-science/openfold3/SKILL.md)
- Structure prediction using OpenFold3, an open-weights PyTorch reproduction of AlphaFold3 from the AlQuraishi Lab. Use this skill when predicting protein/nucleic-acid/ligand complex structures with an Apache-2.0-licensed AF3 reimplementation.

## paper-narrative
- Skill file: [paper-narrative](../../../.local/skill-sources/AcademicForge/skills/claude-science/paper-narrative/SKILL.md)
- Judge and reshape the STORY a paper's figures tell. Input is the work itself — manuscript (or abstract) + figure deck — no hand-written brief. `paper_brief_prompt(abstract, captions)` hands you the prompt to write the brief yourself (pitch/vision/per-figure-claims); then you play a handling editor over the full deck and return hook_verdict (would Fig 1 make me send this for review?), arc (hook→mechanism→evidence→application), figure_moves (panels in the wrong figure), missing_panels (concrete analyses to RUN), kill_list, and boldest_defensible_fig1. Hands per-figure claims to `figure-composer`. Load when writing or revising a paper.

## pdf-explore
- Skill file: [pdf-explore](../../../.local/skill-sources/AcademicForge/skills/claude-science/pdf-explore/SKILL.md)
- Use this skill when the user has attached a PDF, paper, report, or other document and the answer needs content from more than one place in it: summarize the methods or any other section, compare sections, find where a topic is discussed, read a value or label off a figure or chart, or find/list/extract every instance of something across the whole document (datasets, benchmarks, citations, figures, table rows, accession numbers — including appendices). Parses the PDF once with a deterministic Python kernel: `pdf_pages` (pages as persistent text, or high-res images), `pdf_outline` (embedded TOC), `pdf_scan` (a lexical pre-filter that narrows a long doc to candidate pages), `pdf_grep` (regex sweep for exhaustive pattern extraction). You read the shortlist and do the relevance / summary / extraction judgment yourself. For PDF creation/manipulation, use reportlab/pypdf directly.

## product-self-knowledge
- Skill file: [product-self-knowledge](../../../.local/skill-sources/AcademicForge/skills/claude-science/product-self-knowledge/SKILL.md)
- Stop and consult this skill whenever your response would include specific facts about Anthropic's products. Covers: Claude Code (how to install, Node.js requirements, platform/OS support, MCP server integration, configuration), Claude API (function calling/tool use, batch processing, SDK usage, rate limits, pricing, models, streaming), and Claude.ai (Pro vs Team vs Enterprise plans, feature limits). Trigger this even for coding tasks that use the Anthropic SDK, content creation mentioning Claude capabilities or pricing, or LLM provider comparisons. Any time you would otherwise rely on memory for Anthropic product details, verify here instead — your training data may be outdated or wrong.

## proteinmpnn
- Skill file: [proteinmpnn](../../../.local/skill-sources/AcademicForge/skills/claude-science/proteinmpnn/SKILL.md)
- Inverse-fold a protein backbone (PDB structure) into amino-acid sequence with ProteinMPNN (Dauparas et al. 2022, github.com/dauparas/ProteinMPNN). Reach for this skill to run sequence design on RFdiffusion backbones, to redesign one chain of a PDB while holding interface residues fixed, or to generate a temperature-swept set of sequences for downstream folding.

## remote-compute-modal
- Skill file: [remote-compute-modal](../../../.local/skill-sources/AcademicForge/skills/claude-science/remote-compute-modal/SKILL.md)
- Run GPU jobs on the user's own Modal account via host.compute.create('byoc:modal', ...). Covers the create→submit→wait_for_notification flow, the compute_provider kernel for env setup, image/volume resolution, and the two approval cards. Load once you've decided to dispatch to Modal.

## remote-compute-ssh
- Skill file: [remote-compute-ssh](../../../.local/skill-sources/AcademicForge/skills/claude-science/remote-compute-ssh/SKILL.md)
- Submit→wait_for_notification→harvest workflow for the user's SSH/SLURM hosts. Load once you've decided to dispatch remote.

## scgpt
- Skill file: [scgpt](../../../.local/skill-sources/AcademicForge/skills/claude-science/scgpt/SKILL.md)
- Embed and annotate single-cell expression data with scGPT, a foundation model for single-cell biology. Use this skill when: (1) Producing cell embeddings from an AnnData for clustering/integration, (2) Zero-shot or fine-tuned cell-type annotation, (3) Gene-level representation for perturbation/GRN tasks. For probabilistic single-cell models (scVI etc.), use the scvi-tools library.

## scvi-tools
- Skill file: [scvi-tools](../../../.local/skill-sources/AcademicForge/skills/claude-science/scvi-tools/SKILL.md)
- Probabilistic single-cell RNA-seq with scvi-tools — scVI for a batch-corrected latent space, scANVI for semi-supervised label transfer, and Bayesian differential expression. Reach for this skill to integrate scRNA-seq batches, embed cells for clustering, transfer annotations from a reference onto a query, or score differentially expressed genes per cluster. For spatial deconvolution / mapping use the cell2location, DestVI, or Tangram methods instead.

## self-awareness
- Skill file: [self-awareness](../../../.local/skill-sources/AcademicForge/skills/claude-science/self-awareness/SKILL.md)
- Claude Science's own session database schema and SDK surface for introspection via host.query(). Load this when you need to query your own conversation history, token usage, cost accounting, execution log, or artifact metadata beyond what host.frames()/host.artifacts() provide — e.g. "how many tokens has this session used", "what was my last tool call", "list every file I've written", "where are messages stored", "what tables can I query", "inspect frames.context_data", or any time you're about to PRAGMA-probe the Claude Science metadata DB to discover its schema.

## skill-creator
- Skill file: [skill-creator](../../../.local/skill-sources/AcademicForge/skills/claude-science/skill-creator/SKILL.md)
- Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

## solublempnn
- Skill file: [solublempnn](../../../.local/skill-sources/AcademicForge/skills/claude-science/solublempnn/SKILL.md)
- Inverse-fold a backbone with SolubleMPNN — ProteinMPNN retrained on a soluble-PDB subset (Dauparas et al. 2022) — for sequences biased toward cytosolic expression and reduced aggregation. Reach for this skill when designs from vanilla ProteinMPNN are aggregating or going to inclusion bodies, when redesigning a membrane-adjacent fold for soluble expression, or when an E. coli expression screen is the next step.

## using-model-endpoint
- Skill file: [using-model-endpoint](../../../.local/skill-sources/AcademicForge/skills/claude-science/using-model-endpoint/SKILL.md)
- Call a registered model endpoint over its native HTTP API from the endpoint's scoped inference kernel (BASE_URL preloaded). Load once a task needs predictions from a registered model endpoint.

## web-artifacts-builder
- Skill file: [web-artifacts-builder](../../../.local/skill-sources/AcademicForge/skills/claude-science/web-artifacts-builder/SKILL.md)
- Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

## scientific-visualization
- Skill file: [scientific-visualization](../../../.local/skill-sources/AcademicForge/skills/scientific-visualization/SKILL.md)
- Create publication figures with matplotlib/seaborn/plotly. Multi-panel layouts, error bars, significance markers, colorblind-safe, export PDF/EPS/TIFF, for journal-ready scientific plots.
