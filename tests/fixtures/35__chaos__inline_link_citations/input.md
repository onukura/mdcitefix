# Inline Link Citations Test

This document tests handling of citations that include URLs inline using the format [[N](URL)].

## Inline Links Without Reference Definitions

The study by Smith [[1](https://example.com/smith-paper)] shows interesting results.
Another paper [[2](https://example.com/jones-study)] contradicts this finding.
A third source [[3](https://example.com/davis-research)] provides additional context.

## Inline Links That Duplicate Existing References

This citation [[5](https://example.com/smith-paper)] points to the same URL as citation 1.
Another duplicate [[6](https://example.com/jones-study)] should merge with citation 2.

## Mixed: Some Inline, Some Regular

Regular citation [4] here.
Inline citation [[7](https://example.com/new-source)] here.
Another regular citation [8] here.

## Inline Links Should Extract URLs

The format [[1](URL)] should:
1. Extract the URL
2. Add it to reference definitions if missing
3. Merge with existing references if URL matches
4. Renumber based on order of appearance

## References

[4]: https://example.com/wilson-analysis
[8]: https://example.com/chen-insights
