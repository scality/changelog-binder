from click.testing import CliRunner

from changelog_binder import cli


def test_main():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
