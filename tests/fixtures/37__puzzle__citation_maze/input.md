# Citation Maze - Complex Citation Puzzle

This is a maze of citations designed to test the parser's ability to handle complex, intertwined references.

## Section A: Forward and Backward References

First we cite [100, 50, 25] in reverse order.
Then we cite [1] which hasn't been defined yet.
Now we cite [200-205] as a range.
Back to [50] again, and [25, 100] in different order.

## Section B: Overlapping Ranges and Singles

Citations [1-5] overlap with [3, 4, 5, 6, 7].
Then [2;4;6;8;10] with semicolons.
Mix it up: [1, 3-5, 7, 9-11, 13].
Duplicate URL test: [301, 302, 303] all point to same URL.

## Section C: Missing and Found

Cite [404] which is missing.
Cite [999] which will be defined.
Cite [777] which is also missing.
Now [1-3, 5, 7-9, 11] but skip [4, 6, 10].

## Section D: Dense Citation Web

According to [10, 20, 30], building on [5, 15, 25], and contradicting [2, 4, 6, 8],
we find that [1] and [3] support [7] and [9], while [11-15] provide additional context.
However, [16;17;18] suggest otherwise, and [19, 20, 21] complicate matters.

See also [50-55, 60-65, 70-75] for comprehensive coverage.

## Section E: Extreme Mixing

Wild mix: [999, 1, 777, 2, 404, 3, 50, 4, 100, 5, 200, 6].
Range chaos: [1-3, 10-12, 20-22, 30-32, 40-42, 50-52].
Same citations repeated: [1, 1, 1, 2, 2, 3] should deduplicate.

## References

[1]: https://example.com/paper-alpha
[2]: https://example.com/paper-beta
[3]: https://example.com/paper-gamma
[4]: https://example.com/paper-delta
[5]: https://example.com/paper-epsilon
[6]: https://example.com/paper-zeta
[7]: https://example.com/paper-eta
[8]: https://example.com/paper-theta
[9]: https://example.com/paper-iota
[10]: https://example.com/paper-kappa
[11]: https://example.com/paper-lambda
[12]: https://example.com/paper-mu
[13]: https://example.com/paper-nu
[14]: https://example.com/paper-xi
[15]: https://example.com/paper-omicron
[16]: https://example.com/paper-pi
[17]: https://example.com/paper-rho
[18]: https://example.com/paper-sigma
[19]: https://example.com/paper-tau
[20]: https://example.com/paper-upsilon
[21]: https://example.com/paper-phi
[25]: https://example.com/paper-psi
[30]: https://example.com/paper-omega
[50]: https://example.com/review-alpha
[51]: https://example.com/review-beta
[52]: https://example.com/review-gamma
[53]: https://example.com/review-delta
[54]: https://example.com/review-epsilon
[55]: https://example.com/review-zeta
[60]: https://example.com/review-eta
[61]: https://example.com/review-theta
[62]: https://example.com/review-iota
[63]: https://example.com/review-kappa
[64]: https://example.com/review-lambda
[65]: https://example.com/review-mu
[70]: https://example.com/review-nu
[71]: https://example.com/review-xi
[72]: https://example.com/review-omicron
[73]: https://example.com/review-pi
[74]: https://example.com/review-rho
[75]: https://example.com/review-sigma
[100]: https://example.com/book-alpha
[200]: https://example.com/thesis-alpha
[201]: https://example.com/thesis-beta
[202]: https://example.com/thesis-gamma
[203]: https://example.com/thesis-delta
[204]: https://example.com/thesis-epsilon
[205]: https://example.com/thesis-zeta
[301]: https://example.com/duplicate-url
[302]: https://example.com/duplicate-url
[303]: https://example.com/duplicate-url
[999]: https://example.com/future-work
