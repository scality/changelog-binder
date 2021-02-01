from click.testing import CliRunner

from changelog_binder import cli


def test_main():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0


def test_list():
    runner = CliRunner()
    result = runner.invoke(cli.main, ["list"])
    assert result.exit_code == 1


def test_list_in():
    runner = CliRunner()
    result = runner.invoke(cli.main, ["list", "--in", "0.1.0"])
    assert result.exit_code == 1


def test_list_from_to():
    runner = CliRunner()
    result = runner.invoke(
        cli.main, ["list", "--from", "0.1.0", "--to", "0.2.0"]
    )
    assert result.exit_code == 1


def test_list_from():
    runner = CliRunner()
    result = runner.invoke(cli.main, ["list", "--from", "0.1.0"])
    assert result.exit_code == 1


def test_render():
    runner = CliRunner()
    result = runner.invoke(cli.main, ["render"])
    assert result.exit_code == 1
