import click


@click.group()
def main():
    """Main entry-point of the changelog-binder tool"""


@main.command()
@click.option(
    "--in",
    "in_",
    metavar="VERSION",
    help=" ".join(
        [
            "List all fragments included in the given version,",
            "and not in its preceding version",
        ]
    ),
)
@click.option(
    "--from",
    "from_",
    metavar="VERSION",
    help=" ".join(
        [
            "List all fragments from the given version and up to either HEAD",
            "or the version passed using the '--to' argument",
        ]
    ),
)
@click.option(
    "--to",
    metavar="VERSION",
    help="List all fragments up to the given version",
)
def list(in_, from_, to):
    """List fragments that will be rendered"""
    raise NotImplementedError
