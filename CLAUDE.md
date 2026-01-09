# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`mdcitefix` is a Python tool that repairs and normalizes numeric citations and reference definitions in Markdown files. It renumbers citations based on order of appearance, deduplicates URLs, removes unused references, and regenerates reference definition blocks.

## Development Commands

This project uses `uv` for dependency management.

### Setup
```bash
# Install dependencies (including dev dependencies)
uv sync
```

### Testing
```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=mdcitefix

# Run a specific test file
uv run pytest tests/test_basic.py

# Run a specific test function
uv run pytest tests/test_basic.py::test_renumber_attach_defs
```

### Linting
```bash
# Run ruff linter
uv run ruff check

# Auto-fix linting issues
uv run ruff check --fix

# Format code
uv run ruff format
```

### Running the Tool
```bash
# Run from source
uv run python -m mdcitefix.cli input.md

# Or use the main entry point
uv run python main.py
```

## Architecture

The codebase is organized into four main modules:

### `core.py` - Main Processing Pipeline
The central orchestration layer that implements the `fix_markdown()` function. This function:
1. Splits the document into protected (code blocks) and unprotected segments
2. Extracts in-text citations (`[1]`, `[2,3]`) and reference definitions
3. Resolves citations to URLs via reference definitions and optional reference sections
4. Deduplicates citations by normalized URLs (strips tracking params, fragments)
5. Renumbers citations sequentially based on order of first appearance
6. Rewrites in-text citations and regenerates reference definition blocks
7. Optionally generates/updates a `## References` section

Key data structures:
- `FixOptions`: Configuration for processing (dedupe, drop unused refs, compact ranges, etc.)
- `FixReport`: Output report with renumber map, merged keys, missing refs, warnings

### `parse.py` - Document Parsing
Handles extraction of citation elements from markdown:
- `split_protected_segments()`: Splits document into code block vs regular text segments to avoid modifying citations inside code
- `extract_intext_citations()`: Finds `[1]`, `[1,2]`, `[1-3]` style citations using regex, excluding markdown links
- `extract_refdefs()`: Parses reference definitions like `[1]: https://example.com "Title"`
- `extract_reference_section_entries()`: Fallback parser for `## References` sections with numbered list format

### `normalize.py` - URL Normalization
URL canonicalization for deduplication:
- `normalize_url()`: Strips tracking parameters (utm_*, gclid, fbclid), fragments, normalizes trailing slashes, lowercases scheme/netloc
- `compact_ranges()`: Converts `[1, 2, 3, 5]` to `1-3, 5` format when `compact_number_ranges` option is enabled

### `cli.py` - Command Line Interface
Argument parsing and file I/O:
- Supports stdin/stdout or file paths
- Options map to `FixOptions` configuration
- Generates optional JSON report file

## Processing Flow

The key insight is the two-phase approach:
1. **Parse phase**: Extract all citations, definitions, and reference section entries
2. **Rewrite phase**: Apply renumbering map to in-text citations, then regenerate definition blocks

Citations are renumbered based on order of appearance, not their original numbers. Merged citations (same URL) are all updated to point to the kept reference number.
