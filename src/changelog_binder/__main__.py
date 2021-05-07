"""Main entry point for the :program:`changelog-binder` program."""

import argparse
from typing import List, Optional

import changelog_binder


def build_parser() -> argparse.ArgumentParser:
    """Build an :class:`argparse.ArgumentParser` for :program:`changelog-binder`."""
    parser = argparse.ArgumentParser(
        description="""
Generate changelogs and release notes from snippets stored in a project Git repository.
""".strip(),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {}".format(changelog_binder.__version__),
    )

    return parser


def main(args: Optional[List[str]] = None) -> None:
    """Run the :command:`changelog-binder` script."""
    parser = build_parser()
    _ = parser.parse_args(args=args)


if __name__ == "__main__":
    main()
