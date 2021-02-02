import changelog_binder


def test_version():
    assert hasattr(changelog_binder, "__version__")
