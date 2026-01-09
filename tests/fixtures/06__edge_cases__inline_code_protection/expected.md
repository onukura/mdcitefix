# Code Block Protection Test

Citations inside code blocks should not be modified.

## Regular Citations

Normal text citations [1] and [2] should be renumbered.

## Code Blocks

Here's example code:

```python
# This [3] looks like a citation but isn't
data = fetch_data([1, 2, 3])
results = process([4], [5], [6])
```

More discussion referencing actual sources [3] and [4].

## Inline Code

Using `array[1]` or `list[2]` in inline code shouldn't affect citations.
However, real citations [5] should still be processed.

## Mixed Context

```javascript
// Array access: items[3]
function get Items(indices) {
    return indices.map(i => items[i]);
}
```

After the code, we cite the implementation guide [6] and best practices [7].
<!-- mdcitefix:refs -->
[1]: https://example.com/source1
[2]: https://example.com/source2
