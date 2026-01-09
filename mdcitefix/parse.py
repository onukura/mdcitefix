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


def split_protected_segments(
    md: str, warnings: Optional[List[str]] = None
) -> List[Segment]:
    warnings = warnings if warnings is not None else []
    segs: List[Segment] = []

    i = 0
    n = len(md)
    buf = []
    protected = False
    fence = None  # ``` or ~~~
    seg_index = 0

    def flush():
        nonlocal seg_index, buf, protected
        if buf:
            segs.append(Segment(seg_index, protected, "".join(buf)))
            seg_index += 1
            buf = []

    # very small state machine: fence code blocks only
    while i < n:
        # detect fence start/end at line start
        if md.startswith("```", i) or md.startswith("~~~", i):
            # must be line start (or after \n)
            if i == 0 or md[i - 1] == "\n":
                mark = md[i : i + 3]
                if not protected:
                    flush()
                    protected = True
                    fence = mark
                else:
                    if fence == mark:
                        # end fence
                        # include fence line in protected segment
                        # find end of line
                        pass
                # consume full line
                j = md.find("\n", i)
                if j == -1:
                    buf.append(md[i:])
                    i = n
                    if protected:
                        # unclosed fence
                        warnings.append("Unclosed fenced code block; protected to EOF.")
                    flush()
                    return segs
                buf.append(md[i : j + 1])
                i = j + 1
                # toggle on end fence
                if protected and fence == mark:
                    # If this line is an end fence, we need heuristic:
                    # end fence usually has only fence chars + optional spaces
                    # We'll treat any fence line inside protected as potential end when it matches.
                    # To keep it simple: if line is exactly fence + optional spaces
                    pass
                # Heuristic: toggle if this fence line has no extra backticks?
                # We'll do a simpler approach:
                if protected and fence == mark:
                    # If next chars after mark on this line are only spaces/tabs
                    pass
                continue

        # inline code protection: we keep it simple by not splitting; safer to treat it as unprotected.
        # If you want, extend: detect backticks and mark as protected within segment.
        buf.append(md[i])
        i += 1

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
        for m in _CITE_RE.finditer(seg.text):
            keys = _expand_body(m.group("body"))
            if not keys:
                continue
            tokens.append(
                CiteToken(
                    segment_index=seg.index,
                    span_start=m.start(),
                    span_end=m.end(),
                    keys=keys,
                )
            )
    return tokens


_REFDEF_RE = re.compile(
    r'(?m)^\[(?P<k>\d+)\]:\s+(?P<url>\S+)(?:\s+"(?P<title>[^"]+)")?\s*$'
)


def extract_refdefs(md: str) -> Dict[str, Tuple[str, Optional[str], str]]:
    out: Dict[str, Tuple[str, Optional[str], str]] = {}
    for m in _REFDEF_RE.finditer(md):
        k = m.group("k")
        url = m.group("url")
        title = m.group("title")
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
