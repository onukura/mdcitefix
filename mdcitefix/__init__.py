"""mdcitefix - Repair numeric citations and reference definitions in Markdown."""

from .core import FixOptions, FixReport, fix_markdown

__all__ = ["fix_markdown", "FixOptions", "FixReport"]
