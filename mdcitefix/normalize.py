from __future__ import annotations

from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


def normalize_url(url: str) -> str:
    try:
        sp = urlsplit(url.strip())
    except Exception:
        return url.strip()

    scheme = sp.scheme.lower() or "https"
    netloc = sp.netloc.lower()
    path = sp.path or "/"

    # strip fragment
    fragment = ""

    # drop common tracking params
    q = []
    for k, v in parse_qsl(sp.query, keep_blank_values=True):
        lk = k.lower()
        if lk.startswith("utm_") or lk in {"gclid", "fbclid"}:
            continue
        q.append((k, v))
    query = urlencode(q, doseq=True)

    # normalize trailing slash (keep root '/')
    if path != "/" and path.endswith("/"):
        path = path[:-1]

    return urlunsplit((scheme, netloc, path, query, fragment))


def compact_ranges(nums: list[int]) -> str:
    nums = sorted(set(nums))
    if not nums:
        return ""
    parts = []
    a = b = nums[0]
    for x in nums[1:]:
        if x == b + 1:
            b = x
        else:
            parts.append(_range_part(a, b))
            a = b = x
    parts.append(_range_part(a, b))
    return ", ".join(parts)


def _range_part(a: int, b: int) -> str:
    return f"{a}-{b}" if b > a else str(a)
