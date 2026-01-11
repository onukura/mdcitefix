from mdcitefix.core import fix_markdown, FixOptions


def test_renumber_attach_defs():
    md = """
Text [2] then [1].

[1]: https://a.example
[2]: https://b.example
""".strip()

    out, rep = fix_markdown(md, FixOptions(dedupe_by_url=False))
    assert "Text [1] then [2]." in out
    assert "[1]: https://b.example" in out
    assert "[2]: https://a.example" in out


def test_dedupe_same_url():
    md = """
A [1] B [2]

[1]: https://x.example?utm_source=foo
[2]: https://x.example
""".strip()

    out, rep = fix_markdown(md)  # dedupe ON by default
    # URLs are deduplicated (merged in report)
    assert len(rep.merged) == 1
    assert rep.merged[0] == ("2", "1")
    # Only one URL definition remains
    assert out.count("]: https://") == 1


def test_preserve_refdefs_inside_fenced_code_block():
    md = """
```
[1]: https://code.example
```

Text [1]

[1]: https://real.example
""".strip()

    out, rep = fix_markdown(md, FixOptions(dedupe_by_url=False))
    assert "```" in out
    assert "[1]: https://code.example" in out
    assert "[1]: https://real.example" in out


def test_refdef_parsing_supports_angle_and_parentheses_title():
    md = """
Text [1]

[1]: <https://a.example> (Example Title)
""".strip()

    out, rep = fix_markdown(md, FixOptions(dedupe_by_url=False))
    assert '[1]: https://a.example "Example Title"' in out


def test_inline_links_resolve_for_merged_citations():
    md = """
A [1] B [2]

[1]: https://x.example?utm_source=foo
[2]: https://x.example
""".strip()

    out, rep = fix_markdown(md, FixOptions(insert_inline_links=True))
    assert "MISSING_URL" not in out
    assert "[1](" in out
