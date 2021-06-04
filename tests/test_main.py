"""Test the CLI entrypoint of `changelog-binder`."""

import runpy
import sys
from typing import List

import pytest
from pytest_mock import MockerFixture

import changelog_binder


def test_main(mocker: MockerFixture) -> None:
    """Test running the :mod:`changelog_binder` package."""
    mocker.patch("sys.argv", sys.argv[:1])
    # Once for real
    runpy.run_module("changelog_binder", run_name="__main__", alter_sys=True)
    # Once to please the coverage checks
    runpy.run_module("changelog_binder", alter_sys=True)


def _invoke_cli(mocker: MockerFixture, args: List[str]) -> None:
    """Invoke the CLI with given arguments."""
    from changelog_binder.__main__ import main

    mocker.patch("sys.argv", ["changelog-binder"])

    main(args=args)


def test_version(mocker: MockerFixture, capsys: pytest.CaptureFixture[str]) -> None:
    """Test invoking the CLI with `--version`."""
    with pytest.raises(SystemExit):
        _invoke_cli(mocker, ["--version"])

    captured = capsys.readouterr()
    assert captured.out == "changelog-binder {}\n".format(changelog_binder.__version__)
