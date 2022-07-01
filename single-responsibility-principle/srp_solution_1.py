# srp_solution_1.py
# !/usr/bin/env python3
"""The first solution.

Use functions. Each function only has one reason to change.
The functions use simple APIs and can be composed to achieve a larger goal.
"""


import os
from typing import Any, Final, Generator, Tuple

MAX_COLS: Final[int] = 3
LazyEntries = Generator[Tuple[str, str], Any, Any]


def listdir(path: str, seperator=" ") -> str:
    """Returns a value separated string of entries from the path.

    Example: listdir("/path/") -> "file1 file2 dir1 file3"
    """
    return seperator.join(os.listdir(path))


def sort_entries(entries: str, seperator=" ") -> str:
    """Returns a value seperated string of sorted entries."""
    return seperator.join(sorted(entries.split(seperator)))


# No side-effects
def entries_in_column_format(entries: str, seperator=" ") -> LazyEntries:
    """Yields entries in a column format."""
    width = os.get_terminal_size().columns // MAX_COLS

    column = 1
    for entry in entries.split(seperator):
        end_char = ""
        if column == MAX_COLS:
            end_char, column = "\n", 0
        yield f"{entry:<{width}}", end_char
        column += 1


# Isolate side-effects (IO)
def print_entries(entries: str, seperator=" ") -> None:
    """Print entries to standard out."""
    for entry, end_char in entries_in_column_format(entries, seperator):
        print(entry, end=end_char)
    print(end="\n")


if __name__ == "__main__":
    entries = listdir("../")
    print_entries(sort_entries(entries))
