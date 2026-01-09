# Test Fixtures for mdcitefix

This directory contains comprehensive test fixtures for the mdcitefix tool. Each test case is organized as a self-contained directory with input/output pairs and optional configuration.

## Directory Structure

Fixtures use a flat structure with naming convention: `<number>__<category>__<case_name>/`

```
fixtures/
├── 01__edge_cases__simple_renumber/
├── 02__edge_cases__complex_ranges/
├── 08__url_normalization__utm_params/
├── 13__error_handling__missing_urls/
├── 16__real_world__academic_paper/
└── ...
```

Categories:
- **edge_cases**: Edge cases for citation formats and parsing
- **url_normalization**: URL normalization and deduplication tests
- **error_handling**: Error conditions and malformed input
- **real_world**: Realistic usage scenarios
- **performance**: Performance benchmarks

## Fixture Format

Each test case directory contains:

- **input.md** (required): The input markdown document with broken citations
- **expected.md** (required): The expected output after running mdcitefix
- **config.json** (optional): FixOptions configuration for this test case
- **metadata.json** (optional): Test metadata and expected report values

### config.json Format

```json
{
  "dedupe_by_url": true,
  "drop_unused_defs": true,
  "compact_number_ranges": false,
  "ensure_references_section": false,
  "marker": "<!-- mdcitefix:refs -->"
}
```

All fields are optional and will use defaults if not specified.

### metadata.json Format

```json
{
  "description": "Human-readable description of what this test validates",
  "tags": ["edge-case", "renumbering"],
  "expected_report": {
    "missing_count": 0,
    "merged_count": 2,
    "warnings_count": 0
  }
}
```

## Test Cases

### Edge Cases (01-07)

1. **01_simple_renumber**: Basic renumbering by order of appearance
2. **02_complex_ranges**: Range expansion [1-5] and compact_number_ranges option
3. **03_semicolon_separator**: Semicolon-separated citations [1;2;3]
4. **04_mixed_formats**: All citation formats combined
5. **05_unclosed_code_block**: Unclosed fence block handling and warnings
6. **06_inline_code_protection**: Citations in code blocks preserved
7. **07_empty_citations**: Invalid citation formats ignored

### URL Normalization (08-12)

8. **08_utm_params**: UTM parameter stripping and deduplication
9. **09_fragments**: Fragment (#section) removal and deduplication
10. **10_case_normalization**: Scheme and domain case normalization
11. **11_trailing_slash**: Path trailing slash normalization
12. **12_multiple_tracking_params**: Multiple tracking parameters (utm_*, gclid, fbclid)

### Error Handling (13-15)

13. **13_missing_urls**: Citations without definitions generate MISSING_URL
14. **14_malformed_urls**: Unparseable URLs preserved as-is
15. **15_orphaned_citations**: Unused definitions with drop_unused_defs option

### Real World (16-18)

16. **16_academic_paper**: Academic paper with References section
17. **17_tech_article**: Technical blog post with code examples
18. **18_api_documentation**: API documentation with heavy deduplication

### Performance (19-20)

19. **19_medium_500_refs**: Medium document (500 lines, 50 refs)
20. **20_large_1000_refs**: Large document (1000 lines, 100 refs)

## Running Tests

```bash
# Run all fixture tests
uv run pytest tests/test_fixtures.py -v

# Run specific test
uv run pytest tests/test_fixtures.py::test_fixture[01_simple_renumber] -v

# Run tests in a category
uv run pytest tests/test_fixtures.py -k edge_cases

# Run with coverage
uv run pytest tests/test_fixtures.py --cov=mdcitefix
```

## Adding New Test Cases

1. Create a new directory under the appropriate category
2. Add `input.md` and `expected.md` files
3. Optionally add `config.json` for non-default options
4. Optionally add `metadata.json` for documentation
5. The test runner will automatically discover and run the new test

## Naming Conventions

- Directory names: `NN__category__descriptive_name` where NN is a two-digit number
- Double underscores (`__`) separate number, category, and name
- Single underscores (`_`) for multi-word names within each segment
- Keep names concise but descriptive

Examples:
- `01__edge_cases__simple_renumber`
- `08__url_normalization__utm_params`
- `16__real_world__academic_paper`
