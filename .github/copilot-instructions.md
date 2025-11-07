# Copilot Instructions for IMTA Analytics Project

## ⚠️ CRITICAL: Environment Setup
- **ALWAYS activate the conda environment FIRST** before any Python commands
- **MANDATORY**: Run `conda activate imta-analytics` at the start of EVERY shell session
- Use the environment defined in `environment.yml`
- **ALL Python/pip commands MUST be run within the activated conda environment**

## ⚠️ CRITICAL: Git Operations
- **ALWAYS use `git mv` for renaming tracked files** - preserves git history and file tracking
- **NEVER use simple `mv` commands** on tracked files - breaks git history
- **Only use `mv` for untracked files** that haven't been added to git yet
- **Check `git status` first** to verify file tracking status before any move operations

## Coding Standards & Philosophy
- **Avoid excessive error checking** - prefer clean, readable code over defensive programming
- **Trust controlled environments** - validate at boundaries (data load functions, API entry points), not at every internal function
- **Don't create synthetic data** if input datasets are missing - fail gracefully instead
- Follow existing code patterns in the project
- Prioritize clarity over cleverness

### Error Checking Strategy
- **Validate at boundaries**: Check inputs in public API functions and data loaders
- **Trust internal calls**: Skip redundant checks in functions that receive pre-validated data
- **Document assumptions**: Use docstrings to clarify input expectations (e.g., "Assumes data loaded via load_toa5_file()")
- **Example**: `load_toa5_file()` guarantees proper numeric types and datetime TIMESTAMP, so downstream analysis functions don't need to re-check
- **Benefits**: Cleaner code, better performance, clearer contracts between functions

## Project Context
- This is a data science platform for Integrated Multi-Trophic Aquaculture (IMTA) systems
- Key data flows: sensor data (TOA5) → quality control → analysis → predictive modeling
- Main package: `imta_analytics/` (installable via `pip install -e .`)
- Data sources: Campbell Scientific dataloggers (TOA5 format), YSI EXO2 sensors, ADCP current profiles
- Analysis notebooks are in `notebooks/`
- Literature and technical references are in `refs/`

## Development Workflow
- Use pytest for testing: `pytest tests/` (test suite to be created)
- **Follow TDD when feasible**: Write tests for data loaders and analysis functions
- **Pre-commit hooks for fast tests**: Git hooks run unit tests automatically (to be configured)
- Follow the Makefile targets for common operations:
  - `make refs-md` - Convert reference PDFs to markdown
  - `make clean` - Remove build artifacts and caches
- Data format documentation is in `docs/data-format-analysis.md`
- System design docs are in `docs/planning/`
- Package documentation is in `PACKAGE.md`

## Git Operations & Change Tracking
- Use `get_changed_files` tool for checking git status and viewing diffs
- **Automated PR creation is encouraged** - use available GitHub tools for pull request creation
- Prefer GitHub tools over manual git commands when available

### Commit Review Policy
- **ALWAYS PAUSE FOR USER REVIEW before committing changes** made during the current session
- **Stage files first** (`git add`), then **STOP and wait for user approval** before running `git commit`
- **Exception**: Only auto-commit if user explicitly says "commit this" or "go ahead and commit"
- **Show summary**: When staging is complete, show `git diff --cached --stat` and wait for user to review
- **User has final say**: Let user decide when they're ready to commit, don't rush to commit automatically

### Change Documentation Workflow
- **ALWAYS document significant changes in `next_commit.md`** - this file spans chat sessions and maintains a running log of agent modifications
- **Structure changes by category**: Use sections with descriptive headings like "Algorithm Implementation", "Infrastructure Changes", "Testing & Validation", etc.
- **Include technical details**: Line counts, file impacts, method explanations, and validation results
- **Persist across sessions**: The file accumulates changes until commit, allowing comprehensive documentation of multi-session work
- **Post-commit cleanup**: After successful commit, zero out `next_commit.md` to start fresh for next change cycle
- **Use for commit messages**: Extract comprehensive commit messages from accumulated `next_commit.md` content
- **Track incremental progress**: Document both completed changes and work-in-progress for better session continuity
- **Ignore linting errors**: `next_commit.md` is an untracked scratch file - do not waste cycles fixing markdown linting errors in it
- **NEVER stage or commit `next_commit.md`** - this file is intentionally untracked (in .gitignore) and serves only as a scratch pad for documenting changes before commit

## Data Handling
- Real data is in `data/` directory (not tracked in git)
- UNH Aquafort buoy station data is in `data/aquafort-buoy-station/`
- **TOA5 format specifics**:
  - Line 4 contains "Smp" strings that break type inference
  - Use `load_toa5_file()` from `imta_analytics.data` to load correctly
- **Data quality philosophy**: Prefer behavioral heuristics (e.g., detecting cascading identical values) over exhaustive hardcoded error lists for robustness and maintainability
- Always validate data shapes and types at loading boundaries
- Use existing utility functions in `imta_analytics/data/loaders.py`

## Communication Style
- Be concise and technical
- Reference specific files and functions when relevant
- Assume familiarity with marine biology and animal tracking concepts
- Focus on practical solutions over theoretical explanations

## Visualization Standards
- **Prefer single-column timeseries layouts** with `sharex=True` for better temporal correlation
- Use `plt.subplots(n, 1, figsize=(14, 16), sharex=True)` instead of complex grid layouts
- Stack diagnostic plots vertically to align time axes
- Remove plot padding with `ax.set_xlim()` or `ax.margins(x=0)`
- **Use mermaid diagrams for flowcharts and process visualization** - `render_mermaid_diagram()` available in notebook_utils for any flowchart, sequence diagram, or process visualization
- **mermaid-py included in environment.yml** - no additional setup required for diagram rendering

## Notebook Handling
- **NEVER USE copilot_getNotebookSummary tool** - it hangs indefinitely and is explicitly forbidden
- **NEVER attempt to summarize raw/full .ipynb files** - encoded images consume excessive tokens
- **ALWAYS use unix file tools instead** to understand notebook structure: `grep`, `head`, `tail`, `cat`, etc.

## Python Development Tools
- **AVOID mcp_pylance_* tools** - they are slow and inefficient for quick operations
- **PREFER run_in_terminal with python -c** for quick Python code execution and testing
- **USE install_python_packages** for package installation in the correct environment
- **For finding cells**: Use `grep -n "VSCode.Cell" notebook.ipynb` to find cell boundaries and IDs
- **For finding code**: Use `grep -A5 -B5 "function_name"` to find specific code in notebooks
- **For cell content**: Use `grep -A20 "id=\"cell_id\"" notebook.ipynb` to read specific cells
- **For markdown cells**: Use `grep -A10 "language=\"markdown\"" notebook.ipynb`
- **For python cells**: Use `grep -A10 "language=\"python\"" notebook.ipynb`
- **Remove cell outputs before analysis** when possible using `jupyter nbconvert --clear-output`
- **Focus on code content** rather than execution outputs when analyzing notebooks
- **If you catch yourself trying to use copilot_getNotebookSummary, STOP and use grep instead**

## Shell Command Safety
- **AVOID exclamation marks (!) in shell commands** - bash interprets `!` as history expansion which causes command failures
- **Use period (.) instead of exclamation mark** in print statements: `print('Import successful.')` not `print('Import successful!')`
- **Avoid ! in comments** within shell-executed Python code: `# Success` not `# Success!`
- **Test commands safely** by avoiding special characters that trigger shell interpretation

### Notebook Editing Best Practices
- **PREFER edit_notebook_file tool** - this is the primary method for notebook editing and works reliably for content modifications
- **Cell ID vs Ordinal Position**: Most cells do NOT have explicit IDs and instead use implicit cell-order ordinals to match with attachment metadata - "Cell 16" refers to the 16th cell in the .ipynb file, not a cell with id="16"
- **Cell ID handling**: VS Code notebooks have cell IDs even when they appear missing - the edit_notebook_tool can find and use them correctly
- **User references by ordinal**: When users mention "Cell 16", they mean the 16th cell in sequential order, which may or may not have an explicit ID attribute
- **For analysis/understanding**: Use unix tools (`grep`, `python -c` JSON parsing) to understand notebook structure before editing
- **Fallback methods when needed**: If edit_notebook_file fails, can use `grep`/`sed` or Python JSON manipulation as alternatives
- **For major refactoring**: Edit multiple cells sequentially using edit_notebook_file rather than trying to add new cells
- **Verify changes**: Use `grep` or `read_file` to confirm edits were applied correctly after using edit_notebook_file
- **Test functionality**: Run modified cells to ensure changes work as expected

### Notebook Content Standards
- **Focus on analysis, not implementation** - notebooks should present scientific analysis, not code development history
- **Remove implementation details** - eliminate references to API changes, function refactoring, or development iterations
- **No self-congratulatory messaging** - avoid marketing-style language about code quality or implementation improvements
- **Scientific tone** - maintain professional, analytical tone focused on research findings and biological insights
- **Use next_commit.md for development tracking** - document implementation changes in commit messages, not in analysis notebooks
- **Clean presentation** - remove historical comments about code evolution or function updates that don't serve analysis goals

## PDF to Markdown Conversion
- **Use Makefile targets** - `make refs-md` converts all PDFs in refs/ subdirectories
- **Granular conversion**:
  - `make pubs-md` - Convert only `refs/publications/*.pdf`
  - `make tech-md` - Convert only `refs/technical/*.pdf`
- **Manual conversion**: `uvx --with markitdown[all] markitdown input.pdf --output output.md`
- **Preserve original filenames** - change only the extension from `.pdf` to `.md`
- **Cleanup**: `make clean-md` removes all generated markdown files

## Markdown & Documentation Standards
- **Follow markdown linting rules** - ensure clean, consistent formatting
- **Ordered lists**: Each list under a new heading should restart at 1 (avoid MD029 errors)
- **Blank lines**: Surround lists, tables, and headings with blank lines (MD032, MD022, MD058)
- **Fenced code blocks**: Always specify language (`text`, `python`, `yaml`, etc.) to avoid MD040 errors
- **Avoid emphasis as headings**: Use proper heading levels (e.g., H2, H3) instead of bold text for section headers (avoid MD036 errors)
- **Unique headings**: Avoid duplicate heading text at the same or different levels (MD024 errors) - add contextual prefixes to disambiguate (e.g., "StreamingProcessor: Key Methods" vs "PerformanceTelemetry: Key Methods")
- **For query strings/code**: Use fenced code blocks with `text` language instead of italic emphasis (`*text*`)
- **For literature review docs**: Use semantic numbering in content but respect markdown list conventions
- **Check formatting**: Run markdown linter or use editor extensions to catch issues early

## Emoji Usage Policy
- **Professional scientific tone required** - documentation should be pragmatic and grounded in science
- **Remove decorative emojis** - avoid emojis used for visual appeal or to make content "fun" (e.g., 🧲📉💪🐾📁🎯🧭📏⚡🔍)
- **Retain functional symbols** - keep check marks (✅✓), x marks (❌), and similar symbols when they enhance clarity in:
  - Comparison tables (e.g., "Python: ✅" vs "R: ❌")
  - Validation lists (e.g., "✓ Tests pass")
  - Status indicators (e.g., "❌ Known limitation")
- **Unicode range detection**: Use `grep -P '[\x{1F300}-\x{1F9FF}\x{2600}-\x{26FF}\x{2700}-\x{27BF}]'` to find emojis systematically
- **Exception for critical warnings**: ⚠️ acceptable in CRITICAL section headings for emphasis (e.g., "## ⚠️ CRITICAL: Environment Setup")
- **Apply systematically**: When cleaning up documentation, search entire files rather than spot-checking individual sections

## Testing Standards
- **Test structure**: `tests/unit/` for fast tests (~5-10s), `tests/integration/` for slower end-to-end tests
- **Pre-commit hook**: `.git/hooks/pre-commit` runs unit tests automatically before commits
- **Shared fixtures**: Define in `tests/conftest.py` for reuse across test files
- **TDD approach**: Write tests first for new data loaders and analysis functions
- **Keep unit tests fast**: Mock external dependencies (file I/O, network calls)
- **Use parametrize**: Test multiple cases efficiently with `@pytest.mark.parametrize`
- **Test boundaries**: Empty data, NaN values, sensor error codes, physical outliers
- **Run tests**: `pytest tests/unit/` (fast), `pytest tests/` (all), `pytest --cov=imta_analytics` (with coverage)
