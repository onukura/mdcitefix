# URL Deduplication Hell

This puzzle tests the URL normalization and deduplication logic with tricky variations.

## Same URL, Different Tracking Parameters

Citation [1] with no tracking.
Citation [1] with utm_source.
Citation [1] with utm_medium.
Citation [1] with utm_campaign.
Citation [1] with all UTM params.
Citation [1] with fbclid.
Citation [1] with gclid.
Citation [1] with multiple tracking params.

## Same URL, Different Cases

Citation [2] in lowercase.
Citation [2] in UPPERCASE domain.
Citation [2] in MixedCase domain.
Citation [3] in different path case.

## Same URL, Different Fragments

Citation [4] with no fragment.
Citation [4] with #section1.
Citation [4] with #section2.
Citation [4] with #top.

## Same URL, Different Trailing Slashes

Citation [5] with slash.
Citation [5] without slash.
Citation [6] with slash and query.
Citation [6] without slash but with query.

##混合地獄 (Mixed Hell)

All these should deduplicate: [1].
All these should deduplicate: [2].
All these should deduplicate: [4].
All these should deduplicate: [5].

Path case [3] might or might not dedupe depending on implementation.
Query variations [6] should dedupe.

## Really Tricky Ones

Citation [7] with http.
Citation [8] with https (same otherwise).
Citation [9] with www prefix.
Citation [10] without www prefix.

These should NOT dedupe (different protocols): [7, 8].
These might dedupe (www normalization): [9, 10].

## References
<!-- mdcitefix:refs -->
[1]: https://example.com/article
[2]: https://example.com/paper
[3]: https://example.com/Paper
[4]: https://example.com/doc
[5]: https://example.com/page/
[6]: https://example.com/page/?query=value
[7]: http://example.com/resource
[8]: https://example.com/resource
[9]: https://www.example.com/item
[10]: https://example.com/item
