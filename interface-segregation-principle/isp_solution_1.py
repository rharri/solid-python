# isp_solution_1.py
# !/usr/bin/env python3
"""The first solution.

Utilize Python's protocols (i.e. structural subtyping).

Note about @runtime_checkable from PEP-0544:
- "The default semantics is that isinstance() and issubclass() fail for
protocol types. This is in the spirit of duck typing - protocols basically
would be used to model duck typing statically, not explicitly at runtime."
- "The typing module will define a special @runtime_checkable class
decorator ... essentially making them 'runtime protocols'"
"""


from collections import OrderedDict, namedtuple
from typing import Protocol, runtime_checkable

Display = namedtuple("Display", ["size", "ppi"])


@runtime_checkable
class SupportsPrint(Protocol):
    """Protocol for classes that provide print() method."""

    def print(self, from_page: int, to_page: int) -> None:
        """Print one or more pages.

        Args:
            from_page: The page to start printing from (inclusive).
            to_page: The last page that should be printed (inclusive).
        """
        ...


@runtime_checkable
class SupportsPlaySound(Protocol):
    """Protocol for classes that provide play_sound() method."""

    def play_sound(self) -> None:
        ...


@runtime_checkable
class SupportsPlayVideo(Protocol):
    """Protocol for classes that provide play_video() method."""

    def play_video(self) -> None:
        ...


class EBookReader:
    """An e-reader device."""

    def __init__(self, screen_size: Display, storage_size: int) -> None:
        """Inits EBookReader with a display and storage size."""
        self._screen_size: Display = screen_size
        self._storage_size: int = storage_size
        self._zoom_level: int = 100
        self._pages: OrderedDict[int, object] = OrderedDict()
        self._current_page: int = 0
        self._bookmarks: set[int] = set()

    def open(self, path_to_ebook: str) -> None:
        """Open e-book for viewing.

        Args:
            path_to_ebook: A path-like object which is the pathname of the
            e-book to be opened.
        """
        print(f"Opening e-book from {path_to_ebook}")

    def display_page(self) -> None:
        """Displays the current page to the screen."""
        self._pages[self._current_page]

    def previous_page(self) -> None:
        """Go to the previous page.

        This action is relative to the current page.
        """
        self._current_page -= 1

    def next_page(self) -> None:
        """Go to the next page.

        This action is relative to the current page.
        """
        self._current_page += 1

    def add_bookmark(self) -> None:
        """Add a bookmark to the current page."""
        self._bookmarks.add(self._current_page)


# ComicBookReader now opts into the features that is can provide.
# ComicBookReader is not burdened with supporting APIs that it does not
# support or implement.
class ComicBookReader(EBookReader):
    """An e-reader device that is capable of reading comic books."""

    def print(self, from_page: int, to_page: int) -> None:
        """Print one or more pages from the e-book.

        Args:
            from_page: The page to start printing from (inclusive).
            to_page: The last page that should be printed (inclusive).
        """
        print(f"Printing {from_page} to {to_page}")


class KindleReader(EBookReader):
    """An e-reader device that is capable of reading Kindle books."""

    def play_sound(self) -> None:
        """Play the sound on the current page."""
        print("Playing sound")

    def play_video(self) -> None:
        """Play the video on the current page."""
        print("Playing video")

    def print(self, from_page: int, to_page: int) -> None:
        """Print one or more pages from the e-book.

        Args:
            from_page: The page to start printing from (inclusive).
            to_page: The last page that should be printed (inclusive).
        """
        print(f"Printing {from_page} to {to_page}")


if __name__ == "__main__":
    comicbook_reader = ComicBookReader(
        Display(size=6.8, ppi=300), storage_size=8
    )  # noqa
    comicbook_reader.open(r"/storage/old_man_logan.cbt")
    comicbook_reader.print(from_page=25, to_page=30)

    assert isinstance(comicbook_reader, SupportsPrint)

    kindle_reader = KindleReader(Display(size=6, ppi=167), storage_size=4)
    kindle_reader.open("/storage/a_philosophy_of_software_design.azw3")
    kindle_reader.print(from_page=1, to_page=50)
    kindle_reader.play_video()

    assert isinstance(kindle_reader, SupportsPrint)
    assert isinstance(kindle_reader, SupportsPlaySound)
    assert isinstance(kindle_reader, SupportsPlayVideo)
