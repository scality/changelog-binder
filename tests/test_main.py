import sys
from unittest.mock import patch


@patch("changelog_binder.cli.main")
def test___main__(mock_main):
    import changelog_binder.__main__  # noqa: F401

    assert mock_main.called

    del sys.modules["changelog_binder.__main__"]
