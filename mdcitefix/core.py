from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from mdcitefix.normalize import compact_ranges, normalize_url
from mdcitefix.parse import (
    extract_intext_citations,
    extract_refdefs,
    extract_reference_section_entries,
    split_protected_segments,
)


@dataclass(frozen=True)
class FixOptions:
    dedupe_by_url: bool = True
    drop_unused_defs: bool = True
    compact_number_ranges: bool = False
    ensure_references_section: bool = False  # generate/repair "## References" list too
    preserve_inline_links: bool = False  # keep existing [N](URL) format in text
    insert_inline_links: bool = False  # convert [N] to [N](URL) format in text
    marker: str = "<!-- mdcitefix:refs -->"


@dataclass
class FixReport:
    renumber_map: Dict[str, str]
    merged: List[Tuple[str, str]]  # (old_key -> kept_key) before renumber
    missing: List[str]  # cited but no url found
    unused: List[str]  # defined but not cited (if drop_unused_defs=False)
    warnings: List[str]

    def to_json(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False, indent=2)


def fix_markdown(md: str, opt: FixOptions = FixOptions()) -> tuple[str, FixReport]:
    warnings: List[str] = []

    # 1) protect code regions
    segments = split_protected_segments(md, warnings=warnings)

    # 2) parse in-text citations (only from unprotected segments)
    cites = extract_intext_citations(segments)

    # ordered list of citation keys as they appear
    used_keys_ordered: List[str] = []
    for c in cites:
        for k in c.keys:
            if k not in used_keys_ordered:
                used_keys_ordered.append(k)

    # 3) parse refdefs (whole document; but we will later regenerate)
    refdefs = extract_refdefs(md)

    # 4) parse reference section entries (optional backup source)
    refsec = extract_reference_section_entries(md)

    # Build raw key->(url,title)
    key_to_entry: Dict[str, tuple[Optional[str], Optional[str], str]] = {}
    for k, (url, title, raw) in refdefs.items():
        key_to_entry[k] = (url, title, raw)
    for k, (url, title, raw) in refsec.items():
        key_to_entry.setdefault(k, (url, title, raw))

    # Add URLs from inline link citations [N](URL)
    # Inline link URLs take precedence over definitions
    for cite in cites:
        if cite.inline_url:
            for k in cite.keys:
                key_to_entry[k] = (cite.inline_url, None, "")

    # 5) resolve missing keys
    missing: List[str] = []
    for k in used_keys_ordered:
        if k not in key_to_entry or not key_to_entry[k][0]:
            missing.append(k)

    # 6) dedupe by normalized URL (optional)
    merged: List[Tuple[str, str]] = []
    if opt.dedupe_by_url:
        norm_to_kept_key: Dict[str, str] = {}
        new_used: List[str] = []
        for k in used_keys_ordered:
            url = (key_to_entry.get(k) or (None, None, ""))[0]
            if not url:
                # keep missing as-is (still gets number)
                new_used.append(k)
                continue
            norm = normalize_url(url)
            if norm in norm_to_kept_key:
                kept = norm_to_kept_key[norm]
                merged.append((k, kept))
                # do not add duplicate key
            else:
                norm_to_kept_key[norm] = k
                new_used.append(k)
        used_keys_ordered = new_used

    # 7) assign new numbers
    renumber_map: Dict[str, str] = {}
    for i, k in enumerate(used_keys_ordered, start=1):
        renumber_map[k] = str(i)

    # Map merged keys to kept key's new number as well
    merged_key_to_number: Dict[str, str] = {}
    for old, kept in merged:
        if kept in renumber_map:
            merged_key_to_number[old] = renumber_map[kept]

    # Build reverse renumber_map for O(1) lookup (optimization)
    reverse_renumber_map: Dict[str, str] = {v: k for k, v in renumber_map.items()}
    number_to_keys: Dict[str, List[str]] = {}
    for key, number in {**renumber_map, **merged_key_to_number}.items():
        number_to_keys.setdefault(number, []).append(key)

    # 8) rewrite in-text citations (only unprotected segments)
    def map_key(k: str) -> str:
        if k in renumber_map:
            return renumber_map[k]
        if k in merged_key_to_number:
            return merged_key_to_number[k]
        # cited but unknown: still assign stable placeholder number at end
        return k

    new_segments = []
    for seg in segments:
        if seg.protected:
            new_segments.append(seg.text)
            continue
        new_text = seg.text
        # Collect citations for this segment
        seg_cites = [c for c in cites if c.segment_index == seg.index]
        # Sort by position descending to replace from end to start (avoids offset issues)
        seg_cites.sort(key=lambda c: c.span_start, reverse=True)
        for cite in seg_cites:
            mapped_nums = [map_key(k) for k in cite.keys]
            # drop duplicates and sort numerically when possible
            uniq = []
            for x in mapped_nums:
                if x not in uniq:
                    uniq.append(x)
            # try numeric sort if all digits
            if all(u.isdigit() for u in uniq):
                uniq = sorted(uniq, key=lambda s: int(s))
            if opt.compact_number_ranges and all(u.isdigit() for u in uniq):
                body = compact_ranges([int(u) for u in uniq])
            else:
                body = ", ".join(uniq)

            # Determine whether to use inline link format
            use_inline = False
            inline_url = None

            if opt.preserve_inline_links and cite.inline_url:
                # Keep existing inline link format
                use_inline = True
                inline_url = cite.inline_url
            elif opt.insert_inline_links:
                # Convert to inline link format
                use_inline = True
                # Get URL from key_to_entry for the first mapped number
                if uniq:
                    first_key = uniq[0]
                    # Find original key(s) for this mapped number using reverse map
                    orig_key = reverse_renumber_map.get(first_key)
                    candidate_keys = (
                        [orig_key] if orig_key else number_to_keys.get(first_key, [])
                    )
                    for candidate in candidate_keys:
                        if not candidate:
                            continue
                        url_data = key_to_entry.get(candidate, (None, None, ""))
                        if url_data[0]:
                            inline_url = url_data[0]
                            break
                    if inline_url is None:
                        inline_url = "MISSING_URL"

            if use_inline and inline_url:
                new_token = f"[{body}]({inline_url})"
            else:
                new_token = f"[{body}]"

            new_text = (
                new_text[: cite.span_start] + new_token + new_text[cite.span_end :]
            )
        new_segments.append(new_text)

    rewritten = "".join(new_segments)

    # 9) remove existing numeric refdefs (we regenerate)
    rewritten_wo_defs = _strip_numeric_refdefs(rewritten)

    # 10) generate new refdef block at end
    new_defs_lines = [opt.marker]
    # Build new defs from used_keys_ordered + missing
    for old_key in used_keys_ordered:
        new_n = renumber_map[old_key]
        url, title, _raw = key_to_entry.get(old_key, (None, None, ""))
        if not url:
            url = "MISSING_URL"
        if title:
            new_defs_lines.append(f'[{new_n}]: {url} "{title}"')
        else:
            new_defs_lines.append(f"[{new_n}]: {url}")
    new_defs = "\n" + "\n".join(new_defs_lines) + "\n"

    out = rewritten_wo_defs.rstrip() + new_defs

    # 11) optionally (re)create References section
    if opt.ensure_references_section:
        out = _ensure_references_section(
            out, used_keys_ordered, renumber_map, key_to_entry
        )

    # report unused defs if needed
    unused: List[str] = []
    if not opt.drop_unused_defs:
        for k in refdefs.keys():
            if k not in renumber_map and k not in merged_key_to_number:
                unused.append(k)

    report = FixReport(
        renumber_map={
            **renumber_map,
            **{k: v for k, v in merged_key_to_number.items()},
        },
        merged=merged,
        missing=missing,
        unused=unused,
        warnings=warnings,
    )
    return out, report


# ---- internal helpers ----


_REFDEF_RE = re.compile(r"(?m)^\[(\d+)\]:[ \t].*$")


def _strip_numeric_refdefs(md: str) -> str:
    # remove any numeric refdef lines (keep non-numeric refs untouched)
    segments = split_protected_segments(md)
    kept_segments: List[str] = []
    for seg in segments:
        if seg.protected:
            kept_segments.append(seg.text)
            continue
        lines = seg.text.splitlines(True)
        kept_lines = [ln for ln in lines if not _REFDEF_RE.match(ln)]
        kept_segments.append("".join(kept_lines))
    return "".join(kept_segments)


def _ensure_references_section(
    md: str,
    used_keys: List[str],
    renumber: Dict[str, str],
    entries: Dict[str, tuple[Optional[str], Optional[str], str]],
) -> str:
    # naive: replace existing "## References" section if present; else append.
    ref_lines = ["## References", ""]
    for old_key in used_keys:
        n = renumber[old_key]
        url, title, _ = entries.get(old_key, (None, None, ""))
        url = url or "MISSING_URL"
        if title:
            ref_lines.append(f"{n}. {title} — {url}")
        else:
            ref_lines.append(f"{n}. {url}")
    block = "\n".join(ref_lines).rstrip() + "\n"

    # replace existing section
    pattern = re.compile(r"(?ms)^(##\s+References\s*\n.*?)(?=^##\s|\Z)")
    if pattern.search(md):
        return pattern.sub(block, md, count=1)
    else:
        return md.rstrip() + "\n\n" + block
