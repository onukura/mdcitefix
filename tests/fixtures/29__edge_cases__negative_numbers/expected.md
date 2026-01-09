# Negative Numbers Test

This document tests handling of negative numbers in citations.

## Negative Citation Numbers

Regular citations work: [1], [2], [3]
But what about negative: [-1], [-2], [-3]?

## Negative Ranges

Normal range: [1, 2, 3]
Negative range: [-3--1] (from -3 to -1)
Mixed range: [-1-2] (from -1 to 2)?

## Edge Cases with Minus Signs

Double minus: [--1]
Just minus: [-]
Minus in middle: [1--2]
Multiple minuses: [---1]

## Context Matters

Temperature of -20°C [-1] is cold.
Balance: $-500 [2] in debt.
Coordinates: x=-3, y=-5 [3]

## Valid Citations

These should still work normally:
- Citation [1] is valid
- Citation [2] is valid
- Citation [3] is valid
<!-- mdcitefix:refs -->
[1]: https://example.com/first
[2]: https://example.com/second
[3]: https://example.com/third
