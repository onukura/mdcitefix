# Code and Citations Puzzle

This tests how citations interact with code blocks.

## Before and After Code Blocks

Citation before code [1]:

```python
# This [2] should NOT be modified
array[3] = value
citations = [4, 5, 6]
```

Citation after code [1].

## Language-Specific Code Blocks

JavaScript [8]:

```javascript
const refs = [9, 10, 11];
// Citation [12] in comment
```

Python [13]:

```python
data = [14, 15, 16]
# Reference [17]
```

## Inline Code vs Citations

Use `array[2]` for indexing.
But cite paper [2] for details.
Code `[3, 4]` vs citation [3, 4].

## Indented Code Blocks

Normal text [5].

    # Indented code block
    array[6] = "should not change"
    citations = [7, 8, 9]

Back to normal [10].

## Mixed Code and Text

According to [11], the following works:

```
plain code block
[2] should stay as is
no language specified
```

But [12] here should renumber.

## Triple Backticks in Nested Structures

1. List item [13]

   ```python
   code = [28]  # protected
   ```

   Text [14] should renumber.

2. Another item [15]

## Code Blocks with Citation-Like Patterns

```json
{
  "references": [30, 31, 32],
  "citations": "[33]",
  "array": [34, 35]
}
```

Real citations: [16, 17, 18, 19, 20, 21].

## Inline Code Everywhere

The `[11]` in code vs [11] citation.
Multiple `[12]`, `[22]`, `[23]` in code, then [12, 22, 23] citations.

## Unclosed Code Blocks Edge Case

This is normal text [24].

```python
# Code started [37]
array[38] = value

And this continues outside? [39] <!-- fence not closed -->

```

Citation after closing [25].

## Fence Confusion

Normal text [26].

````
```
nested fence [42]
```
````

Citation [27] outside.

## References
<!-- mdcitefix:refs -->
[1]: https://example.com/ref7
[2]: https://example.com/ref18
[3]: https://example.com/ref19
[4]: https://example.com/ref20
[5]: https://example.com/ref21
[6]: https://example.com/ref22
[7]: https://example.com/ref23
[8]: https://example.com/ref24
[9]: https://example.com/ref25
[10]: https://example.com/ref26
[11]: https://example.com/ref1
[12]: https://example.com/ref2
[13]: https://example.com/ref27
[14]: https://example.com/ref28
[15]: https://example.com/ref29
[16]: https://example.com/ref30
[17]: https://example.com/ref31
[18]: https://example.com/ref32
[19]: https://example.com/ref33
[20]: https://example.com/ref34
[21]: https://example.com/ref35
[22]: https://example.com/ref3
[23]: https://example.com/ref4
[24]: https://example.com/ref36
[25]: https://example.com/ref40
[26]: https://example.com/ref41
[27]: https://example.com/ref42
