# Empty/Invalid Citations Test

Tests that invalid citation formats are ignored.

## Valid Citations

Normal citations [1] and [2] work fine.

## Invalid Formats

Empty brackets [] should be ignored.
Non-numeric [abc] should be ignored.
Decimal numbers [1.5] should be ignored.

## Markdown Links

This is a [link](https://example.com) not a citation.
This is a [reference link][ref] also not a citation.

## More Valid Citations

Continuing with valid citations [3] and [4].


[ref]: https://example.com/link
<!-- mdcitefix:refs -->
[1]: https://example.com/valid1
[2]: https://example.com/valid2
[3]: https://example.com/valid3
[4]: https://example.com/valid4
