try:
    import importlib.metadata as importlib_metadata
except ImportError:
    # Python < 3.8, fallback to backported package
    import importlib_metadata  # type: ignore

try:
    __version__ = importlib_metadata.version("changelog-binder")
except importlib_metadata.PackageNotFoundError:
    __version__ = "unknown"
