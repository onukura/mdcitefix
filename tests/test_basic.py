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

