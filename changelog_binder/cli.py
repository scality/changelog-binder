import click

import changelog_binder
import changelog_binder.types


@click.group()
@click.version_option(changelog_binder.__version__)
def main():
    """Main entry-point of the changelog-binder tool"""


def with_list_options(obj):
    decorators = [
        click.option(
            "--to",
            metavar="VERSION",
            help="List all fragments up to the given version",
        ),
        click.option(
            "--from",
            "from_",
            metavar="VERSION",
            help=" ".join(
                [
                    "List all fragments from the given version and up to",
                    "either HEAD or the version passed using the '--to'",
                    "argument",
                ]
            ),
        ),
        click.option(
            "--in",
            "in_",
            metavar="VERSION",
            help=" ".join(
                [
                    "List all fragments included in the given version,",
                    "and not in its preceding version",
                ]
            ),
        ),
    ]

    for decorator in decorators:
        obj = decorator(obj)

    return obj


@main.command()
@with_list_options
def list(in_, from_, to):
    """List fragments that will be rendered"""
    raise NotImplementedError


@main.command()
@with_list_options
@click.option(
    "--release-notes",
    "release_notes",
    is_flag=True,
    help="Only render fragments tagged as release notes entries",
)
@click.option(
    "--kind",
    "kinds",
    type=click.Choice(
        kind.name.lower() for kind in changelog_binder.types.Kind
    ),
    multiple=True,
    help="Only render fragments of given kind(s)",
)
@click.option(
    "--epic",
    "epics",
    multiple=True,
    help="Only render fragments of given epic(s)",
)
@click.option(
    "--no-epic",
    "no_epic",
    is_flag=True,
    help="Only render fragments without specified epic",
)
@click.option(
    "-o",
    "--output",
    type=click.Choice(
        fmt.name.lower() for fmt in changelog_binder.types.OutputFormat
    ),
    default="restructuredtext",
    help="Output format",
)
def render(in_, from_, to, release_notes, kinds, epics, no_epic, output):
    """Render the changelog from fragments"""
    raise NotImplementedError
