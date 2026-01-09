from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .core import FixOptions, fix_markdown


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="mdcitefix", description="Repair numeric citations + refdefs in Markdown."
    )
    p.add_argument("input", help="Input markdown file (or - for stdin).")
    p.add_argument(
        "-o",
        "--output",
        help="Output file (default: overwrite input; stdin => stdout).",
    )
    p.add_argument("--report", help="Write JSON report to file.")
    p.add_argument("--no-dedupe", action="store_true")
    p.add_argument("--keep-unused-defs", action="store_true")
    p.add_argument("--compact-ranges", action="store_true")
    p.add_argument("--ensure-references-section", action="store_true")
    args = p.parse_args(argv)

    opt = FixOptions(
        dedupe_by_url=not args.no_dedupe,
        drop_unused_defs=not args.keep_unused_defs,
        compact_number_ranges=args.compact_ranges,
        ensure_references_section=args.ensure_references_section,
    )

    if args.input == "-":
        md = sys.stdin.read()
        out, rep = fix_markdown(md, opt)
        sys.stdout.write(out)
    else:
        in_path = Path(args.input)
        md = in_path.read_text(encoding="utf-8")
        out, rep = fix_markdown(md, opt)
        if args.output:
            Path(args.output).write_text(out, encoding="utf-8")
        else:
            in_path.write_text(out, encoding="utf-8")

    if args.report:
        Path(args.report).write_text(rep.to_json(), encoding="utf-8")

    # --check 的な用途にするなら、missing があれば exit 1 なども追加するとCIで便利
    return 0
