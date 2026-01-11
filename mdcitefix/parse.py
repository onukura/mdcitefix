from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass(frozen=True)
class Segment:
    index: int
    protected: bool
    text: str


@dataclass(frozen=True)
class CiteToken:
    segment_index: int
    span_start: int
    span_end: int
    keys: List[str]  # old numbers as strings
    inline_url: Optional[str] = None  # URL if citation is in [N](URL) format


def split_protected_segments(
    md: str, warnings: Optional[List[str]] = None
) -> List[Segment]:
    warnings = warnings if warnings is not None else []
    segs: List[Segment] = []
    buf: List[str] = []
    protected = False
    fence: Optional[str] = None
    seg_index = 0

    def flush() -> None:
        nonlocal seg_index, buf, protected
        if buf:
            segs.append(Segment(seg_index, protected, "".join(buf)))
            seg_index += 1
            buf = []

    fence_re = re.compile(r"^ {0,3}([`~]{3,})(.*)$")

    for line in md.splitlines(True):
        match = fence_re.match(line)
        if match:
            marker = match.group(1)
            rest = match.group(2)
            if not protected:
                flush()
                protected = True
                fence = marker
                buf.append(line)
                continue
            if (
                fence
                and marker[0] == fence[0]
                and len(marker) >= len(fence)
                and rest.strip() == ""
            ):
                buf.append(line)
                flush()
                protected = False
                fence = None
                continue

        buf.append(line)

    flush()
    if protected:
        warnings.append(
            "Reached EOF inside fenced code block; protected segment may be incomplete."
        )
    return segs


# In-text citation: [1], [1,2], [1-3], excluding link syntax: []( ) or [][] or [N]:
# Note: \s includes newlines, so use [ \t] to only match spaces/tabs (not newlines)
_CITE_RE = re.compile(
    r"\[(?P<body>\d+(?:\s*(?:,|;)\s*\d+|\s*[-–]\s*\d+)*)\](?![ \t]*[\(\[]|[ \t]*:)"
)

# Inline link citation: [1](URL) or [1, 2](URL)
_INLINE_LINK_CITE_RE = re.compile(
    r"\[(?P<body>\d+(?:\s*(?:,|;)\s*\d+|\s*[-–]\s*\d+)*)\]\((?P<url>[^\)]+)\)"
)


def _expand_body(body: str) -> List[str]:
    body = body.strip()
    if "-" in body or "–" in body:
        parts = re.split(r"\s*[-–]\s*", body)
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            a, b = int(parts[0]), int(parts[1])
            if a <= b and (b - a) <= 5000:  # sanity
                return [str(x) for x in range(a, b + 1)]
    # comma/semicolon list
    nums = re.split(r"\s*(?:,|;)\s*", body)
    out = []
    for x in nums:
        x = x.strip()
        if x.isdigit():
            out.append(x)
    return out


def extract_intext_citations(segments: List[Segment]) -> List[CiteToken]:
    tokens: List[CiteToken] = []
    for seg in segments:
        if seg.protected:
            continue

        # First, extract inline link citations [N](URL)
        inline_matches = []
        for m in _INLINE_LINK_CITE_RE.finditer(seg.text):
            keys = _expand_body(m.group("body"))
            if not keys:
                continue
            url = m.group("url").strip()
            tokens.append(
                CiteToken(
                    segment_index=seg.index,
                    span_start=m.start(),
                    span_end=m.end(),
                    keys=keys,
                    inline_url=url,
                )
            )
            inline_matches.append((m.start(), m.end()))

        # Then extract regular citations [N], excluding overlaps with inline links
        for m in _CITE_RE.finditer(seg.text):
            # Check if this match overlaps with any inline link match
            overlaps = False
            for start, end in inline_matches:
                if not (m.end() <= start or m.start() >= end):
                    overlaps = True
                    break
            if overlaps:
                continue

            keys = _expand_body(m.group("body"))
            if not keys:
                continue
            tokens.append(
                CiteToken(
                    segment_index=seg.index,
                    span_start=m.start(),
                    span_end=m.end(),
                    keys=keys,
                    inline_url=None,
                )
            )
    return tokens


_REFDEF_RE = re.compile(
    r'(?m)^\[(?P<k>\d+)\]:\s+(?P<url><[^>]+>|\S+)'
    r'(?:\s+(?:"(?P<title_dq>[^"]+)"|\'(?P<title_sq>[^\']+)\'|\((?P<title_paren>[^)]+)\)))?\s*$'
)


def extract_refdefs(md: str) -> Dict[str, Tuple[str, Optional[str], str]]:
    out: Dict[str, Tuple[str, Optional[str], str]] = {}
    for m in _REFDEF_RE.finditer(md):
        k = m.group("k")
        url = m.group("url")
        if url.startswith("<") and url.endswith(">"):
            url = url[1:-1]
        title = m.group("title_dq") or m.group("title_sq") or m.group("title_paren")
        out[k] = (url, title, m.group(0))
    return out


def extract_reference_section_entries(
    md: str,
) -> Dict[str, Tuple[str, Optional[str], str]]:
    """
    Very pragmatic: find a 'References' heading and try to extract numbered URLs.
    Returns key->(url,title,raw). keys are the *numbers as written* if found.
    """
    out: Dict[str, Tuple[str, Optional[str], str]] = {}
    # locate section
    sec = re.search(r"(?im)^##\s+References\s*$", md)
    if not sec:
        return out
    start = sec.end()
    # until next heading or EOF
    tail = md[start:]
    m2 = re.search(r"(?im)^##\s+", tail)
    block = tail[: m2.start()] if m2 else tail

    # numbered list: "1. title — url" or "1. url"
    line_re = re.compile(r"(?m)^\s*(?P<k>\d+)[\.\)]\s+(?P<rest>.+?)\s*$")
    url_re = re.compile(r"(https?://\S+)")
    for lm in line_re.finditer(block):
        k = lm.group("k")
        rest = lm.group("rest")
        um = url_re.search(rest)
        if not um:
            continue
        url = um.group(1).rstrip(").,;")
        title = rest[: um.start()].strip(" —-–\t") or None
        out.setdefault(k, (url, title, lm.group(0)))
    return out
