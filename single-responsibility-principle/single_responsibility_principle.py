# single_reponsibility_principle.py
# !/usr/bin/env python3
"""A demonstration of the single responsibility principle

Quotes:
- "The single responsibility principle (SRP) instructs developers to write
code that has one and only one reason to change. If a class has more than
one reason to change, it has more than one responsibility."

Source: Adaptive Code, Second Edition (Microsoft Press, 2017)

This example was inspired by Linux and the Unix Philosophy
(Digital Press, 2003).
"""


import os
from typing import Final

MAX_COLS: Final[int] = 3


# ListDir has more than one reason to change (e.g. sorting predicate,
# print format, etc.)
# ListDir has more than one reason to change and therefore has too many
# responsibilities.
class ListDir:
    """Represents a command for listing entries of a directory."""

    def __init__(self, path: str = None) -> None:
        """Inits ListDir with a path.

        Args:
            path: The path to list.
        """
        self._path = path or os.getcwd()

    def set_path(self, path: str = None) -> None:
        """Sets the current path.

        Args:
            path: The path to list.
        """
        self._path = path or os.getcwd()

    def print(self) -> None:
        """Prints the entries of the current path to standard out.

        The entries are sorted in ascending order and printed in a
        column format.
        """
        entries = sorted(os.listdir(self._path))
        width = os.get_terminal_size().columns // MAX_COLS

        column = 1
        for entry in entries:
            end_char = ""
            if column == MAX_COLS:
                end_char, column = "\n", 0
            print(f"{entry:<{width}}", end=end_char)
            column += 1
        print(end="\n")

    def to_file(self) -> None:
        pass

    def __len__(self) -> int:
        """Returns the number of entries in the current path."""
        return len(os.listdir(self._path))


if __name__ == "__main__":
    ls = ListDir("../")
    ls.print()
    print(len(ls))
