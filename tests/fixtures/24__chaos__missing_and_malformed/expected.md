# Missing and Malformed Citations

## Introduction

This document is a complete mess. It has citations to non-existent references [1],
[2], [3], and also references that exist [4], [5].

Some URLs are malformed or missing [6], [7]. We also have duplicates of the same
URL with different numbers [8], [8], [8] all pointing to the same place.

## Code Examples

Here's some code that should NOT be modified:

```python
# This is a code block - citations here should be protected
def process_data(items):
    # Reference [1] in comment should not be changed
    results = []
    for i in range(len(items)):  # [0] is first item
        if items[i] > threshold[2]:  # [2] should not be a citation
            results.append(items[i])
    return results[3]  # [3] is just array indexing
```

But outside the code block, [4] and [5] should be updated. The undefined
citations [1], [2], [3] will generate warnings.

## More Content

Valid references [4], [5] mixed with invalid [1], [2].
Duplicates [8], [8], [8] should be merged.

Inline code like `array[6]` should not be treated as citation.
But this [6] outside backticks should be (even though it has no definition).

## Unclosed Code Block

```javascript
function broken() {
    // This code block is never closed [1000]
    // So these citations [2000] might cause issues
    return "unclosed";
```

But we continue the document anyway. References [4], [5], [8] appear here.
Missing references [1], [2], [3], [6] also reappear.

## Malformed URLs

The reference [9] has a completely broken URL.
The reference [10] has no URL at all.
The reference [11] has an empty URL.

But [4] and [5] are fine.

## Duplicates Everywhere

Same URL: [8], [8], [8] all identical.
Another set: [12], [12], [12] also identical.

Mixed with valid unique citations [4], [5] and missing ones [1], [2].

[300]:
<!-- mdcitefix:refs -->
[1]: MISSING_URL
[2]: MISSING_URL
[3]: MISSING_URL
[4]: https://example.com/valid-reference-1 "This is fine"
[5]: https://example.com/valid-reference-2
[6]: MISSING_URL
[7]: MISSING_URL
[8]: https://example.com/duplicate-url "First instance"
[9]: htpt://broken:url:scheme "Malformed URL"
[10]: MISSING_URL
[11]: MISSING_URL
[12]: https://example.com/another-duplicate "First instance"
