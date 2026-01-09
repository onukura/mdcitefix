# Markdown Syntax Nightmare

This tests how citations interact with various Markdown syntax elements.

## Citations in Emphasis

**Bold citation [1]** and *italic citation [2]*.
***Bold italic citation [3]***.
**Bold with [link text](https://example.com) and citation [1]**.

## Citations in Blockquotes

> This is a quote with citation [4].
> > Nested quote with citation [5].
> Back to first level [4].

## Citations vs Links

This is a citation [6].
This is [a link](https://example.com).
This is [a link with text [7]](https://example.com).
This is [7] or is it [a reference link][7]?

## Citations in Inline Code

In code: `array[8]` should not be a citation.
But this [8] outside code should be.
More code: `dict["key"][9]` with [9] citation after.

## Escaped Brackets

Escaped: \[10\] should not be a citation.
But this [10] should be.
Half escaped: \[11] and [11\].

## Citations in Lists

- List item [12]
  - Nested item [13]
    - Deep nested [14]
- Another item [12, 13, 14]

1. Numbered item [15]
2. Second item [16]
   1. Sub item [17]

## Citations in Headers

### Header with Citation [18]

#### Another Header [19] and [20]

## Mixed Madness

**Bold [1]** in *italic [2]* with `code[3]` and [3] citation.
> Quote [4] with **bold [5]** and *italic [6]*.

See [link](https://example.com) and citation [7].
Check `inline[8]` vs [8] citation.

## HTML Comments

<!-- This has [21] in comment -->
This has [21] outside comment.

<!-- Citation [22]
multiline comment
should be ignored -->
But [22] here should work.

## References

[1]: https://example.com/bold
[2]: https://example.com/italic
[3]: https://example.com/bold-italic
[4]: https://example.com/quote1
[5]: https://example.com/quote2
[6]: https://example.com/citation
[7]: https://example.com/ambiguous
[8]: https://example.com/array
[9]: https://example.com/dict
[10]: https://example.com/escaped
[11]: https://example.com/half-escaped
[12]: https://example.com/list1
[13]: https://example.com/list2
[14]: https://example.com/list3
[15]: https://example.com/num1
[16]: https://example.com/num2
[17]: https://example.com/num3
[18]: https://example.com/header1
[19]: https://example.com/header2
[20]: https://example.com/header3
[21]: https://example.com/comment1
[22]: https://example.com/comment2
