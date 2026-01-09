# Citation Maze - Complex Citation Puzzle

This is a maze of citations designed to test the parser's ability to handle complex, intertwined references.

## Section A: Forward and Backward References

First we cite [1, 2, 3] in reverse order.
Then we cite [4] which hasn't been defined yet.
Now we cite [5, 6, 7, 8, 9, 10] as a range.
Back to [2] again, and [1, 3] in different order.

## Section B: Overlapping Ranges and Singles

Citations [4, 11, 12, 13, 14] overlap with [12, 13, 14, 15, 16].
Then [11, 13, 15, 17, 18] with semicolons.
Mix it up: [4, 16, 19].
Duplicate URL test: [20] all point to same URL.

## Section C: Missing and Found

Cite [21] which is missing.
Cite [22] which will be defined.
Cite [23] which is also missing.
Now [14, 24] but skip [13, 15, 18].

## Section D: Dense Citation Web

According to [18, 25, 26], building on [3, 14, 27], and contradicting [11, 13, 15, 17],
we find that [4] and [12] support [16] and [28], while [19, 24, 27, 29, 30] provide additional context.
However, [31, 32, 33] suggest otherwise, and [25, 34, 35] complicate matters.

See also [50-55, 60-65, 70-75] for comprehensive coverage.

## Section E: Extreme Mixing

Wild mix: [1, 2, 4, 5, 11, 12, 13, 14, 15, 21, 22, 23].
Range chaos: [1-3, 10-12, 20-22, 30-32, 40-42, 50-52].
Same citations repeated: [4, 11, 12] should deduplicate.

## References
<!-- mdcitefix:refs -->
[1]: https://example.com/book-alpha
[2]: https://example.com/review-alpha
[3]: https://example.com/paper-psi
[4]: https://example.com/paper-alpha
[5]: https://example.com/thesis-alpha
[6]: https://example.com/thesis-beta
[7]: https://example.com/thesis-gamma
[8]: https://example.com/thesis-delta
[9]: https://example.com/thesis-epsilon
[10]: https://example.com/thesis-zeta
[11]: https://example.com/paper-beta
[12]: https://example.com/paper-gamma
[13]: https://example.com/paper-delta
[14]: https://example.com/paper-epsilon
[15]: https://example.com/paper-zeta
[16]: https://example.com/paper-eta
[17]: https://example.com/paper-theta
[18]: https://example.com/paper-kappa
[19]: https://example.com/paper-nu
[20]: https://example.com/duplicate-url
[21]: MISSING_URL
[22]: https://example.com/future-work
[23]: MISSING_URL
[24]: https://example.com/paper-lambda
[25]: https://example.com/paper-upsilon
[26]: https://example.com/paper-omega
[27]: https://example.com/paper-omicron
[28]: https://example.com/paper-iota
[29]: https://example.com/paper-mu
[30]: https://example.com/paper-xi
[31]: https://example.com/paper-pi
[32]: https://example.com/paper-rho
[33]: https://example.com/paper-sigma
[34]: https://example.com/paper-tau
[35]: https://example.com/paper-phi
