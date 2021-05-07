"""changelog_binder: generate changelogs and release notes from VCS.

Tooling to generate changelogs and release notes from snippets stored in a
project Git_ repository, compatible with the GitWaterFlow_ branching model.

.. _Git: https://git-scm.com/
.. _GitWaterFlow: https://dl.acm.org/doi/10.1145/2993274.2993277
"""

import sys
from typing import Callable, cast

if sys.version_info >= (3, 8):
    from importlib.metadata import Distribution, distribution
else:
    from importlib_metadata import Distribution, distribution


__metadata__ = cast(Callable[[str], Distribution], distribution)(__name__).metadata
__license__ = __metadata__["License"]
"""Package license identifier.
.. versionadded:: 0.0.1
"""
__version__ = __metadata__["Version"]
"""Package version identifier.
.. versionadded:: 0.0.1
"""
del __metadata__
