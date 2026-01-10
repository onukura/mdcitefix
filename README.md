# mdcitefix

A Python tool that repairs and normalizes numeric citations and reference definitions in Markdown files.

## What it does

`mdcitefix` automatically:

- **Renumbers citations** based on order of appearance in your document
- **Deduplicates URLs** by normalizing tracking parameters and fragments
- **Removes unused references** that aren't cited in the text
- **Regenerates reference definition blocks** with proper formatting
- **Preserves code blocks** to avoid modifying citations in examples
- **Supports inline citation links** `[1](https://example.com)` format

## Installation

Requires Python 3.10 or later.

### For users

**Using pip:**

```bash
# From PyPI (once published)
pip install mdcitefix

# Or install directly from GitHub
pip install git+https://github.com/onukura/mdcitefix.git
```

**Using uv:**

```bash
# Add to your project (once published to PyPI)
uv add mdcitefix

# Or add directly from GitHub
uv add git+https://github.com/onukura/mdcitefix.git
```

### For developers

```bash
# Clone the repository
git clone https://github.com/onukura/mdcitefix.git
cd mdcitefix

# Install dependencies
uv sync
```

## Quick Start

**If you installed via pip or uv add:**

```bash
# Fix a markdown file in place
mdcitefix input.md

# Read from stdin, write to stdout
cat input.md | mdcitefix - > output.md

# Specify output file
mdcitefix input.md -o output.md

# Generate a JSON report
mdcitefix input.md --report report.json
```

**If running from source (developers):**

```bash
# Fix a markdown file in place
uv run python -m mdcitefix.cli input.md

# Or with the mdcitefix command after uv sync
uv run mdcitefix input.md
```

## Example

**Before:**

```markdown
This is from source [2] and this from [1].

[1]: https://example.com?utm_source=twitter
[2]: https://example.com
[3]: https://unused.com
```

**After:**

```markdown
This is from source [1] and this from [2].

[1]: https://example.com
[2]: https://example.com
```

Note how:

- Citations are renumbered based on order of appearance (2→1, 1→2)
- Duplicate URLs are merged (tracking params removed)
- Unused reference [3] is removed

## Options

| Option | Description |
|--------|-------------|
| `--no-dedupe` | Disable URL deduplication (keep all references even if URLs match) |
| `--keep-unused-defs` | Keep reference definitions that aren't cited in the text |
| `--compact-ranges` | Compact number ranges (e.g., `[1, 2, 3]` → `[1-3]`) |
| `--ensure-references-section` | Generate/update a `## References` section |
| `--preserve-inline-links` | Preserve existing `[N](URL)` format in text |
| `--insert-inline-links` | Convert all citations to `[N](URL)` format |
| `-o, --output FILE` | Output file (default: overwrite input; stdin → stdout) |
| `--report FILE` | Write JSON report to file |

## How it works

1. **Parse**: Splits document into protected (code blocks) and unprotected segments
2. **Extract**: Finds in-text citations (`[1]`, `[2,3]`) and reference definitions
3. **Resolve**: Maps citations to URLs via reference definitions
4. **Normalize**: Canonicalizes URLs (strips tracking params, fragments, etc.)
5. **Deduplicate**: Merges citations with identical normalized URLs
6. **Renumber**: Assigns new numbers based on order of first appearance
7. **Rewrite**: Updates in-text citations and regenerates reference blocks

### URL Normalization

When deduplicating, URLs are normalized by:

- Removing tracking parameters (`utm_*`, `gclid`, `fbclid`)
- Stripping fragments (`#section`)
- Normalizing trailing slashes
- Lowercasing scheme and domain

## Development

This project uses `uv` for dependency management.

### Running tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=mdcitefix

# Run specific test
uv run pytest tests/test_basic.py::test_renumber_attach_defs
```

### Linting and formatting

```bash
# Check code
uv run ruff check

# Auto-fix issues
uv run ruff check --fix

# Format code
uv run ruff format
```

## Architecture

The codebase is organized into four main modules:

- **`core.py`**: Main processing pipeline (`fix_markdown()` function)
- **`parse.py`**: Document parsing (citations, reference definitions, sections)
- **`normalize.py`**: URL normalization and deduplication
- **`cli.py`**: Command-line interface

See [CLAUDE.md](CLAUDE.md) for detailed architecture documentation.

## License

MIT
