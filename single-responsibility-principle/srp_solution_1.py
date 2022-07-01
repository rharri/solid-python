# srp_solution_1.py
# !/usr/bin/env python3
"""The first solution.

Use functions. Each function only has one reason to change.
The functions use simple APIs and can be composed to achieve a larger goal.
"""


import os
from typing import Final

MAX_COLS: Final[int] = 3


def listdir(path: str, seperator=" ") -> str:
    """Returns a value separated string of entries from the path."""
    return seperator.join(os.listdir(path))


def sort_entries(entries: str, seperator=" ") -> str:
    """Returns a sorted value seperated string of entries."""
    return seperator.join(sorted(entries.split(seperator)))


def print_entries_in_columns(entries: str, seperator=" ") -> None:
    """Prints entries in a column format."""
    width = os.get_terminal_size().columns // MAX_COLS

    column = 1
    for entry in entries.split(seperator):
        end_char = ""
        if column == MAX_COLS:
            end_char, column = "\n", 0
        print(f"{entry:<{width}}", end=end_char)
        column += 1
    print(end="\n")


def count_entries(entries: str, seperator=" ") -> int:
    """Retruns a count of the value seperated entries."""
    return len(entries.split(seperator))


if __name__ == "__main__":
    entries = listdir("../")
    print_entries_in_columns(sort_entries(entries))
    print(count_entries(entries))
