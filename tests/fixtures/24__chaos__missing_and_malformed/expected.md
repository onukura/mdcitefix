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

But outside the code block, [1] and [2] should be updated. The undefined
citations [404], [999], [1234] will generate warnings.

## More Content

Valid references [1], [2] mixed with invalid [404], [999].
Duplicates [10], [20], [30] should be merged.

Inline code like `array[5]` should not be treated as citation.
But this [5] outside backticks should be (even though it has no definition).

## Unclosed Code Block

```javascript
function broken() {
    // This code block is never closed [1000]
    // So these citations [2000] might cause issues
    return "unclosed";
```

But we continue the document anyway. References [1], [2], [10] appear here.
Missing references [404], [999], [1234], [5] also reappear.

## Malformed URLs

The reference [100] has a completely broken URL.
The reference [200] has no URL at all.
The reference [300] has an empty URL.

But [1] and [2] are fine.

## Duplicates Everywhere

Same URL: [10], [20], [30] all identical.
Another set: [11], [21], [31] also identical.

Mixed with valid unique citations [1], [2] and missing ones [404], [999].

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
