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

[1]: https://one.example.com
[2]: https://two.example.com
[3]: https://three.example.com
[4]: https://four.example.com
[5]: https://five.example.com
[6]: https://six.example.com
[7]: https://seven.example.com
[8]: https://eight.example.com
[9]: https://nine.example.com
[10]: https://ten.example.com
[11]: https://eleven.example.com
<!-- mdcitefix:refs -->
