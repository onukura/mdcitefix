# Extreme Whitespace Test

This document tests handling of excessive whitespace in citations.

## Single Citation with Spaces

Normal: [1]
Single space: [ 2 ]
Multiple spaces: [  3  ]
Extreme spaces: [    4    ]
Tab characters: [	5	]

## Multiple Citations with Spaces

Normal: [1, 2, 3]
Spaced: [ 1 , 2 , 3 ]
Extra spaced: [  1  ,  2  ,  3  ]
Extreme: [    1    ,    2    ,    3    ]

## Ranges with Spaces

Normal: [1-3]
Spaced: [ 1 - 3 ]
Extra spaced: [  1  -  3  ]
Extreme: [    1    -    4    ]

## Mixed Separators with Spaces

Semicolon: [ 1 ; 2 ; 3 ]
Mixed: [ 1 , 2 ; 3 ]

## Asymmetric Spacing

Left heavy: [    1, 2, 3]
Right heavy: [1, 2, 3    ]
Middle heavy: [1    ,    2    ,    3]

## Newlines (should NOT work as citations)

With newline: [1
2]
Multiple newlines: [1

3]

## References

[1]: https://example.com/one
[2]: https://example.com/two
[3]: https://example.com/three
[4]: https://example.com/four
[5]: https://example.com/five
