# Broken Markdown

Unclosed code block [1]:

```python
def foo():
    return [2]
# No closing backticks!

This citation [3] is after unclosed code block.

Unclosed emphasis *this is italic [4] still going...

Unclosed link [this link never closes [5]

Malformed table [6]:

| Column 1 | Column 2
| --- | ---
| Missing pipe [7] | Value
| Value | Missing closing

Nested brackets [[[8]]] and [[[9].

Unclosed quote > This is a quote [10]
> Still quoting [11]
No closing
<!-- mdcitefix:refs -->
