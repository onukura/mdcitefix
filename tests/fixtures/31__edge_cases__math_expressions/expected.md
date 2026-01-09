# Math Expressions Test

This document tests handling of math-like expressions in brackets.

## Arithmetic Operators

Addition: [1+2], [3+4+5]
Subtraction: [10-5], [20-10-5]
Multiplication: [2*3], [4*5*6]
Division: [10/2], [20/4/5]
Modulo: [10%3], [100%7]

## Mixed Operators

Complex: [1+2*3], [10-5/2], [(1+2)*3]
Parentheses: [(1+2)], [(3*4)]

## Assignment-like

Equals: [x=5], [y=10]
Comparison: [x>5], [y<10], [z==3]

## Valid Citations Mixed In

Before math [1] after math.
Between [2+3] and [2] is difference.
Citation [3] should work fine.

## Bitwise-like

AND: [1&2], [3&4]
OR: [1|2], [3|4]
XOR: [1^2], [3^4]

## Valid References
<!-- mdcitefix:refs -->
[1]: https://example.com/first
[2]: https://example.com/second
[3]: https://example.com/third
