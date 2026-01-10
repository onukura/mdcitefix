# Inline Link Citations Test

This document tests handling of citations that include URLs inline using the format [[N](URL)].

## Inline Links Without Reference Definitions

The study by Smith [[1]] shows interesting results.
Another paper [[2]] contradicts this finding.
A third source [[3]] provides additional context.

## Inline Links That Duplicate Existing References

This citation [[4]] points to the same URL as citation 1.
Another duplicate [[2]] should merge with citation 2.

## Mixed: Some Inline, Some Regular

Regular citation [6] here.
Inline citation [[5]] here.
Another regular citation [7] here.

## Inline Links Should Extract URLs

The format [[1]] should:
1. Extract the URL
2. Add it to reference definitions if missing
3. Merge with existing references if URL matches
4. Renumber based on order of appearance

## References
<!-- mdcitefix:refs -->
[1]: URL
[2]: https://example.com/jones-study
[3]: https://example.com/davis-research
[4]: https://example.com/smith-paper
[5]: https://example.com/new-source
[6]: https://example.com/wilson-analysis
[7]: https://example.com/chen-insights
