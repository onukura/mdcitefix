# Code and Citations Puzzle

This tests how citations interact with code blocks.

## Before and After Code Blocks

Citation before code [1]:

```python
# This [2] should NOT be modified
array[3] = value
citations = [4, 5, 6]
```

Citation after code [7].

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

Use `array[18]` for indexing.
But cite paper [18] for details.
Code `[19, 20]` vs citation [19, 20].

## Indented Code Blocks

Normal text [21].

    # Indented code block
    array[22] = "should not change"
    citations = [23, 24, 25]

Back to normal [26].

## Mixed Code and Text

According to [1], the following works:

```
plain code block
[2] should stay as is
no language specified
```

But [2] here should renumber.

## Triple Backticks in Nested Structures

1. List item [27]

   ```python
   code = [28]  # protected
   ```

   Text [28] should renumber.

2. Another item [29]

## Code Blocks with Citation-Like Patterns

```json
{
  "references": [30, 31, 32],
  "citations": "[33]",
  "array": [34, 35]
}
```

Real citations: [30, 31, 32, 33, 34, 35].

## Inline Code Everywhere

The `[1]` in code vs [1] citation.
Multiple `[2]`, `[3]`, `[4]` in code, then [2, 3, 4] citations.

## Unclosed Code Blocks Edge Case

This is normal text [36].

```python
# Code started [37]
array[38] = value

And this continues outside? [39] <!-- fence not closed -->

```

Citation after closing [40].

## Fence Confusion

Normal text [41].

````
```
nested fence [42]
```
````

Citation [42] outside.

## References
<!-- mdcitefix:refs -->
