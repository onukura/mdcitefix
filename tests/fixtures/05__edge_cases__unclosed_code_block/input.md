# Unclosed Code Block Test

Tests handling of unclosed fence blocks.

## Normal Section

Regular citations [1] work here.

## Code Example

```python
# This code block is never closed
# Citations like [2] inside should be protected
def example():
    return [3, 4, 5]

## This Looks Like a Header

But it's still inside the unclosed code block.
Citations [6] here should also be protected.

[1]: https://example.com/ref1
[2]: https://example.com/ref2
[3]: https://example.com/ref3
