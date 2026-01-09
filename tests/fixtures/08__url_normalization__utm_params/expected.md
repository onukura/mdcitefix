# UTM Parameter Normalization Test

This document tests URL normalization with UTM tracking parameters.
URLs that differ only by UTM parameters should be deduplicated.

## Social Media Links

The article was shared widely on Twitter [1] and also on
LinkedIn [1]. Both links point to the same content.

## Email Campaign

The email newsletter [1] linked to the same article, as did
the follow-up email [1].

## Direct Links

Some users accessed the article directly [1] without any
tracking parameters.

## Organic Search

Search engines indexed the page [2], which is the canonical URL.

## Mixed References

Throughout the document, we reference the same source [1], [1],
[1], [1], [1], and [2] multiple times. After normalization,
these should all point to a single reference.

## Another Distinct Article

This is a completely different article [3] that should remain separate.

## Third Article

Yet another source [4] with its own UTM parameters.

## Cross-References

Comparing findings from the main article [1] with the second article [3]
and the third article [4] reveals interesting patterns.
<!-- mdcitefix:refs -->
[1]: https://example.com/article?utm_source=twitter&utm_medium=social&utm_campaign=spring2024
[2]: https://example.com/article?ref=organic
[3]: https://example.com/other-article?utm_source=twitter
[4]: https://different.com/page?utm_campaign=promo&param=value
