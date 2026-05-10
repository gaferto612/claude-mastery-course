# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is a **course / educational repository**, not a software product. The deliverable is the content itself: nine numbered markdown modules (`01-introduction` … `09-resources`), an interactive single-file hub (`hub.html`), and runnable Python/TypeScript examples in `06-api-development/examples/` and `08-real-world-projects/code/`. There is no build step, no package manifest, and no application to run — readers either browse the markdown, open `hub.html` directly in a browser, or run individual example scripts standalone.

## Validation (matches `.github/workflows/validate.yml`)

CI runs three checks on every PR to `main`. Reproduce them locally before pushing:

```bash
# 1. Python syntax check — every .py file must compile
python -m compileall -q 06-api-development/examples 08-real-world-projects/code

# 2. TypeScript type check — strict mode, no emit
npm install --no-save @anthropic-ai/sdk typescript @types/node
npx tsc --noEmit --target es2022 --module esnext --moduleResolution bundler \
  --strict --skipLibCheck --allowImportingTsExtensions --types node \
  06-api-development/examples/*.ts

# 3. Markdown internal link check — every relative link must resolve to a real file
# (see validate.yml for the exact shell loop; it greps `](./...)` style links
# in all *.md and fails if the target path doesn't exist on disk)
```

There is no test runner, no linter config, and no formatter — "code must run" is enforced only by the syntax/type checks above.

## Running the examples

Examples are **standalone scripts**, not a package. Each is run directly:

```bash
pip install anthropic                              # for *.py
npm install @anthropic-ai/sdk && npm install -D tsx typescript  # for *.ts
export ANTHROPIC_API_KEY="sk-ant-..."

python 06-api-development/examples/01-hello-world.py
npx tsx 06-api-development/examples/08-streaming.ts
```

`docs/` is in `.gitignore` because Project 2 (`08-real-world-projects/code/project2_doc_qa.py`) expects users to drop their own files there locally — do not commit anything under `docs/`.

## Content conventions (from CONTRIBUTING.md)

When editing course material:

- **Real prompts > generic advice.** Show concrete examples, not abstract description.
- **Note tradeoffs.** Don't just document the happy path.
- **Date-sensitive claims** (model versions, prices, capabilities) must link to an official source so readers can verify when the page goes stale.
- **Every code example must run as written** with the documented setup — the CI syntax checks catch broken code, but semantic breakage (wrong model name, removed API param) is on the author.
- New Module 08 projects should stay **under ~150 lines** with clear setup steps.

## Cross-module structure to preserve

The modules form a directed course graph documented in `README.md` (the "Course map" and "Suggested learning paths" tables). Two implications when making changes:

1. **Relative links between modules are load-bearing** and are CI-enforced. Renaming or moving a file under `0N-*/` will break links from sibling modules, the root `README.md`, and `hub.html`. Run the markdown link check after any rename.
2. **`hub.html` is a self-contained mirror** of the course navigation — it embeds module titles, progress tracking, and a model picker as a single static HTML file (no build, no JS bundler). If you add or rename a module, update `hub.html` to match.

The `assets/` directory holds the SVG banner/divider used by `README.md`; module READMEs should keep using these rather than introducing per-module imagery.

## Git workflow

Always pull and merge before starting work and before pushing:

```bash
git pull origin <branch-name>     # always pull first; merge (do not rebase) any incoming changes
```

Never force-push. Resolve merge conflicts by merging — do not discard remote work.
