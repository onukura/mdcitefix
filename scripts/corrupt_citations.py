#!/usr/bin/env python3
"""
Intentionally corrupt Markdown citations to generate test cases

Usage:
    python scripts/corrupt_citations.py <fixture_dir>

Example:
    python scripts/corrupt_citations.py tests/real_world_fixtures/1706.03762

Corruption strategies:
    1. Shuffle citation numbers randomly
    2. Duplicate URLs with different reference numbers
    3. Add URL tracking parameters (utm_*, fbclid, etc.)
    4. Remove some reference definitions
    5. Add fragments to URLs
    6. Change citation order to not match first appearance
"""

import argparse
import random
import re
import sys
from pathlib import Path
from typing import Dict


def extract_reference_defs(text: str) -> Dict[int, str]:
    """Extract reference definitions ([1]: URL "Title" format)"""
    refs = {}
    pattern = r'^\[(\d+)\]:\s*(\S+)(?:\s+"([^"]*)")?'

    for match in re.finditer(pattern, text, re.MULTILINE):
        num = int(match.group(1))
        url = match.group(2)
        title = match.group(3) or ""
        refs[num] = f"{url}||{title}"  # Store URL and title

    return refs


def extract_list_references(text: str) -> Dict[int, str]:
    """Extract list-style references (- [1] Author. Title. format)"""
    refs = {}
    lines = text.split("\n")
    in_references = False
    current_num = None
    current_content = []

    for line in lines:
        # Detect References section
        if re.match(r"^##\s+References?\s*$", line, re.IGNORECASE):
            in_references = True
            continue

        # End of references section
        if (
            in_references
            and line.startswith("## ")
            and not re.match(r"^##\s+References?\s*$", line, re.IGNORECASE)
        ):
            # Save last entry
            if current_num is not None:
                refs[current_num] = "\n".join(current_content)
            break

        if in_references:
            # Match list item with number: - [1]
            match = re.match(r"^-\s*\[(\d+)\]", line)
            if match:
                # Save previous entry
                if current_num is not None:
                    refs[current_num] = "\n".join(current_content)

                # Start new entry
                current_num = int(match.group(1))
                # Get the rest of the line after [N]
                rest = re.sub(r"^-\s*\[\d+\]\s*", "", line)
                current_content = [rest] if rest.strip() else []
            elif current_num is not None and line.strip():
                # Continuation of current entry
                current_content.append(line)

    # Save last entry if still in references section
    if current_num is not None:
        refs[current_num] = "\n".join(current_content)

    return refs


def add_url_tracking_params(url: str, variation: int = 0) -> str:
    """Add tracking parameters to URL (only params that mdcitefix will strip)"""
    tracking_params = [
        f"utm_source=test&utm_medium=organic&utm_campaign=var{variation}",
        f"fbclid=IwAR{variation}xyz123",
        f"gclid=Cj0KCQ{variation}wBhD",
        f"utm_content=test{variation}&utm_term=keyword",
    ]

    separator = "&" if "?" in url else "?"
    return url + separator + random.choice(tracking_params)


def add_url_fragment(url: str, variation: int = 0) -> str:
    """Add fragment to URL"""
    fragments = [
        f"section-{variation}",
        f"heading{variation}",
        f"ref{variation}",
        "top",
    ]

    # Replace existing fragment if present
    url_base = url.split("#")[0]
    return url_base + "#" + random.choice(fragments)


def corrupt_list_references(content: str, refs: Dict[int, str]) -> str:
    """Corrupt list-style references (simpler, no URL modifications)"""
    lines = content.split("\n")
    output_lines = []
    in_references_section = False

    # Create shuffle mapping for citation numbers
    citation_nums = sorted(refs.keys())
    shuffled_nums = citation_nums.copy()
    random.shuffle(shuffled_nums)
    shuffle_map = dict(zip(citation_nums, shuffled_nums))

    for line in lines:
        # Detect ## References section
        if re.match(r"^##\s+References?\s*$", line, re.IGNORECASE):
            in_references_section = True
            output_lines.append(line)
            continue

        # End of references section (next ## heading)
        if (
            in_references_section
            and line.startswith("## ")
            and not re.match(r"^##\s+References?\s*$", line, re.IGNORECASE)
        ):
            in_references_section = False

        # Skip reference list items in references section (will regenerate)
        if in_references_section and re.match(r"^-\s*\[\d+\]", line):
            continue

        # Shuffle citation numbers in body text
        if not in_references_section:

            def replace_citation(match):
                # Exclude Markdown links
                full_match_end = match.end()
                if full_match_end < len(line) and line[full_match_end] == "(":
                    return match.group(0)

                nums_str = match.group(1)
                # Handle multiple numbers
                if "," in nums_str or "-" in nums_str:
                    nums = []
                    for part in nums_str.split(","):
                        part = part.strip()
                        if "-" in part:
                            start, end = map(int, part.split("-"))
                            nums.extend(range(start, end + 1))
                        else:
                            nums.append(int(part))

                    # Replace with shuffled numbers
                    new_nums = [shuffle_map.get(n, n) for n in nums]
                    return "[" + ", ".join(map(str, new_nums)) + "]"
                else:
                    num = int(nums_str)
                    new_num = shuffle_map.get(num, num)
                    return f"[{new_num}]"

            pattern = r"\[(\d+(?:(?:\s*,\s*|\s*-\s*)\d+)*)\]"
            line = re.sub(pattern, replace_citation, line)

        output_lines.append(line)

    # Regenerate References section in random order
    if in_references_section:
        # Get shuffled numbers in random order
        shuffled_in_random_order = sorted(
            shuffle_map.values(), key=lambda x: random.random()
        )

        # Drop some references (~10%)
        nums_to_include = [n for n in shuffled_in_random_order if random.random() > 0.1]

        for num in nums_to_include:
            # Find original number
            orig_num = None
            for k, v in shuffle_map.items():
                if v == num:
                    orig_num = k
                    break

            if orig_num and orig_num in refs:
                content_text = refs[orig_num]
                output_lines.append(f"- [{num}]")
                # Add content lines
                for content_line in content_text.split("\n"):
                    if content_line.strip():
                        output_lines.append(content_line)

    return "\n".join(output_lines)


def corrupt_citations(content: str, refs: Dict[int, str]) -> str:
    """Intentionally corrupt citations"""
    lines = content.split("\n")
    output_lines = []
    in_references_section = False

    # Create shuffle mapping for citation numbers
    citation_nums = sorted(refs.keys())
    shuffled_nums = citation_nums.copy()
    random.shuffle(shuffled_nums)
    shuffle_map = dict(zip(citation_nums, shuffled_nums))

    # Duplicate some references (assign different numbers to same URL)
    duplicate_refs = {}
    if len(citation_nums) >= 3:
        # Randomly select 2-3 references to duplicate
        num_duplicates = random.randint(2, min(3, len(citation_nums)))
        for i in range(num_duplicates):
            orig_num = random.choice(citation_nums)
            new_num = max(citation_nums) + i + 1
            duplicate_refs[new_num] = refs[orig_num]

    for line in lines:
        # Detect ## References section
        if re.match(r"^##\s+References?\s*$", line, re.IGNORECASE):
            in_references_section = True
            output_lines.append(line)
            continue

        # Special handling for References section
        if in_references_section:
            # End when next section (line starting with ##) appears
            if line.startswith("## ") and not re.match(
                r"^##\s+References?\s*$", line, re.IGNORECASE
            ):
                in_references_section = False
            # Skip reference definition lines (will regenerate later)
            elif re.match(r"^\[\d+\]:", line):
                continue

        # Shuffle citation numbers in body text
        if not in_references_section:

            def replace_citation(match):
                # Exclude Markdown links
                full_match_end = match.end()
                if full_match_end < len(line) and line[full_match_end] == "(":
                    return match.group(0)

                nums_str = match.group(1)
                # Handle multiple numbers
                if "," in nums_str or "-" in nums_str:
                    # Decompose into individual numbers
                    nums = []
                    for part in nums_str.split(","):
                        part = part.strip()
                        if "-" in part:
                            start, end = map(int, part.split("-"))
                            nums.extend(range(start, end + 1))
                        else:
                            nums.append(int(part))

                    # Replace with shuffled numbers
                    new_nums = [shuffle_map.get(n, n) for n in nums]

                    # Randomly mix in duplicate numbers
                    if duplicate_refs and random.random() < 0.1:
                        new_nums.append(random.choice(list(duplicate_refs.keys())))

                    # Return comma-separated (no range compression)
                    return "[" + ",".join(map(str, new_nums)) + "]"
                else:
                    num = int(nums_str)
                    new_num = shuffle_map.get(num, num)

                    # Randomly replace with duplicate number
                    if duplicate_refs and random.random() < 0.05:
                        new_num = random.choice(list(duplicate_refs.keys()))

                    return f"[{new_num}]"

            pattern = r"\[(\d+(?:(?:\s*,\s*|\s*-\s*)\d+)*)\]"
            line = re.sub(pattern, replace_citation, line)

        output_lines.append(line)

    # Regenerate References section (in corrupted state)
    if in_references_section:
        output_lines.append("")

        # Add reference definitions in shuffled order
        all_refs = {**refs, **duplicate_refs}

        # All numbers including shuffle map and duplicates
        all_nums = list(shuffle_map.values()) + list(duplicate_refs.keys())

        # Drop some reference definitions (10% probability)
        nums_to_include = [n for n in all_nums if random.random() > 0.1]

        # Sort in random order (not appearance order)
        nums_to_include.sort(key=lambda x: random.random())

        for num in nums_to_include:
            # First search from original references
            orig_num = None
            for k, v in shuffle_map.items():
                if v == num:
                    orig_num = k
                    break

            if orig_num and orig_num in refs:
                url_title = refs[orig_num]
                url, title = url_title.split("||", 1)

                # Randomly apply URL modification strategies
                strategy = random.randint(0, 4)
                if strategy == 0:
                    # Add tracking parameters
                    url = add_url_tracking_params(url, num)
                elif strategy == 1:
                    # Add fragment
                    url = add_url_fragment(url, num)
                elif strategy == 2:
                    # Add both
                    url = add_url_tracking_params(url, num)
                    url = add_url_fragment(url, num)
                # else: keep original (preserve original URL)

                if title:
                    output_lines.append(f'[{num}]: {url} "{title}"')
                else:
                    output_lines.append(f"[{num}]: {url}")
            elif num in duplicate_refs:
                # Duplicate reference
                url_title = duplicate_refs[num]
                url, title = url_title.split("||", 1)

                # Modify URL
                strategy = random.randint(0, 2)
                if strategy == 0:
                    url = add_url_tracking_params(url, num)
                elif strategy == 1:
                    url = add_url_fragment(url, num)

                if title:
                    output_lines.append(f'[{num}]: {url} "{title}"')
                else:
                    output_lines.append(f"[{num}]: {url}")

    return "\n".join(output_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Intentionally corrupt citations in expected.md to create input.md"
    )
    parser.add_argument(
        "fixture_dir",
        type=Path,
        help="Path to fixture directory containing expected.md",
    )
    parser.add_argument(
        "--seed", type=int, help="Random seed for reproducible corruption"
    )

    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    # Read expected.md
    expected_file = args.fixture_dir / "expected.md"
    if not expected_file.exists():
        print(f"Error: {expected_file} not found", file=sys.stderr)
        print("Create expected.md first", file=sys.stderr)
        sys.exit(1)

    content = expected_file.read_text(encoding="utf-8")

    # Extract reference definitions (try URL format first)
    refs = extract_reference_defs(content)
    ref_format = "url"

    # If no URL-style refs found, try list format
    if not refs:
        refs = extract_list_references(content)
        ref_format = "list"

    if not refs:
        print(f"Warning: No reference definitions found in {expected_file}")
        print("This file may not have numeric citations to corrupt")
        print("Copying expected.md to input.md as-is")
        input_file = args.fixture_dir / "input.md"
        input_file.write_text(content, encoding="utf-8")
        sys.exit(0)

    print(f"Found {len(refs)} references ({ref_format} format)")

    # Corrupt citations based on format
    if ref_format == "list":
        corrupted = corrupt_list_references(content, refs)
        corruptions = [
            "Shuffled citation numbers",
            "Randomized reference list order",
            "Removed some references (~10%)",
        ]
    else:
        corrupted = corrupt_citations(content, refs)
        corruptions = [
            "Shuffled citation numbers",
            "Added duplicate URLs with different numbers",
            "Added URL tracking parameters",
            "Added URL fragments",
            "Randomized reference definition order",
            "Removed some reference definitions (~10%)",
        ]

    # Save as input.md
    input_file = args.fixture_dir / "input.md"
    input_file.write_text(corrupted, encoding="utf-8")

    print(f"✓ Created corrupted input.md at {input_file}")
    print()
    print("Corruptions applied:")
    for corruption in corruptions:
        print(f"  - {corruption}")
    print()
    print("Next steps:")
    print(f"  1. Review {input_file}")
    print(
        f"  2. Run test: uv run pytest tests/test_fixtures.py -k {args.fixture_dir.name}"
    )
    print(f"  3. If test fails, adjust expected.md or config.json as needed")


if __name__ == "__main__":
    main()
