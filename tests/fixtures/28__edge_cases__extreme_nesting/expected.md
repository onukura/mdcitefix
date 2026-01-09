# Extreme Nesting Test

This document tests how nested brackets are handled.

## Double Brackets

Normal citation: [1]
Double brackets: [[2]]
Triple brackets: [[[3]]]
Quadruple brackets: [[[[4]]]]

## Mixed Nesting

Text with [[1]] nested and [2] normal citation.
Complex: [[[1]]] and [[2]] and [[[3]]].

## Expected Behavior

Only the innermost valid numeric citation should be recognized.
So [[1]] should extract citation [1], [[[2]]] should extract [2], etc.

Multiple in sequence: [[1]][[2]][[3]]

## Edge Cases

Empty nested: [[]]
Nested with text: [[citation]]
Nested with link: [[[example](https://example.com)]]
<!-- mdcitefix:refs -->
[1]: https://example.com/first
[2]: https://example.com/second
[3]: https://example.com/third
[4]: https://example.com/fourth
