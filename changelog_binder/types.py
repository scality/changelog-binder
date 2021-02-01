import enum


class Kind(enum.Enum):
    """Kind (of change) of a fragment"""

    FEATURE = enum.auto()
    BUGFIX = enum.auto()
    IMPROVEMENT = enum.auto()


class OutputFormat(enum.Enum):
    """Output format the tool can generate"""

    RESTRUCTUREDTEXT = enum.auto()
