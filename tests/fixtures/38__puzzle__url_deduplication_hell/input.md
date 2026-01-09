# URL Deduplication Hell

This puzzle tests the URL normalization and deduplication logic with tricky variations.

## Same URL, Different Tracking Parameters

Citation [1] with no tracking.
Citation [2] with utm_source.
Citation [3] with utm_medium.
Citation [4] with utm_campaign.
Citation [5] with all UTM params.
Citation [6] with fbclid.
Citation [7] with gclid.
Citation [8] with multiple tracking params.

## Same URL, Different Cases

Citation [10] in lowercase.
Citation [11] in UPPERCASE domain.
Citation [12] in MixedCase domain.
Citation [13] in different path case.

## Same URL, Different Fragments

Citation [20] with no fragment.
Citation [21] with #section1.
Citation [22] with #section2.
Citation [23] with #top.

## Same URL, Different Trailing Slashes

Citation [30] with slash.
Citation [31] without slash.
Citation [32] with slash and query.
Citation [33] without slash but with query.

##混合地獄 (Mixed Hell)

All these should deduplicate: [1, 2, 3, 4, 5, 6, 7, 8].
All these should deduplicate: [10, 11, 12].
All these should deduplicate: [20, 21, 22, 23].
All these should deduplicate: [30, 31].

Path case [13] might or might not dedupe depending on implementation.
Query variations [32, 33] should dedupe.

## Really Tricky Ones

Citation [100] with http.
Citation [101] with https (same otherwise).
Citation [102] with www prefix.
Citation [103] without www prefix.

These should NOT dedupe (different protocols): [100, 101].
These might dedupe (www normalization): [102, 103].

## References

[1]: https://example.com/article
[2]: https://example.com/article?utm_source=twitter
[3]: https://example.com/article?utm_medium=social
[4]: https://example.com/article?utm_campaign=spring2024
[5]: https://example.com/article?utm_source=twitter&utm_medium=social&utm_campaign=spring2024
[6]: https://example.com/article?fbclid=IwAR1234567890abcdef
[7]: https://example.com/article?gclid=Cj0KCQ1234567890
[8]: https://example.com/article?utm_source=google&gclid=Cj0KCQ1234567890&fbclid=IwAR1234567890abcdef

[10]: https://example.com/paper
[11]: https://EXAMPLE.COM/paper
[12]: https://Example.Com/paper
[13]: https://example.com/Paper

[20]: https://example.com/doc
[21]: https://example.com/doc#section1
[22]: https://example.com/doc#section2
[23]: https://example.com/doc#top

[30]: https://example.com/page/
[31]: https://example.com/page
[32]: https://example.com/page/?query=value
[33]: https://example.com/page?query=value

[100]: http://example.com/resource
[101]: https://example.com/resource
[102]: https://www.example.com/item
[103]: https://example.com/item
