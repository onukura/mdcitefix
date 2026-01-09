# Duplicate Reference Definitions

## Problem Statement

This document has the same reference number pointing to different URLs
multiple times. This tests how the tool handles conflicting definitions.

## Main Content

The first paper [1] discusses the methodology, while the second study [2]
provides empirical evidence. A third analysis [3] synthesizes both approaches.

We also cite [1] again here, and [2] multiple times. The work in [3] is
foundational. Additional references include [4], [5], and [6].

The controversial paper [7] sparked debate, later addressed by [8].
Follow-up work [9] and [10] explored implications.

## Analysis

Comparing [1], [2], and [3] reveals interesting patterns. The data from [4]
supports claims in [5], while [6] presents counterarguments.

Recent work [7, 8, 9] has challenged traditional assumptions. The meta-analysis
in [10] attempts to reconcile these conflicts.

<!-- Multiple definitions for same keys - tool should use first or merge somehow -->
[1]: https://example.com/first-definition-for-1
[1]: https://example.com/DUPLICATE-second-def-for-1 "This is a duplicate [1]!"
[2]: https://example.com/original-study
[1]: https://example.com/DUPLICATE-third-def-for-1 "Yet another [1]"
[3]: https://example.com/synthesis-paper
[2]: https://example.com/DUPLICATE-different-url-for-2
[4]: https://example.com/data-source
[5]: https://example.com/supporting-evidence
[3]: https://example.com/DUPLICATE-synthesis-again
[6]: https://example.com/counterargument
[7]: https://example.com/controversial
[7]: https://example.com/DUPLICATE-controversial-again "Duplicate [7]"
[8]: https://example.com/response-paper
[9]: https://example.com/followup-1
[10]: https://example.com/meta-analysis
[5]: https://example.com/DUPLICATE-evidence-different
[9]: https://example.com/DUPLICATE-followup-different
[10]: https://example.com/DUPLICATE-meta-different
