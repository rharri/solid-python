# interface_segregation_principle.py
# !/usr/bin/env python3
"""A demonstration of the interface segregation principle

This demonstration is based on Robert C. Martin's paper titled,
"Design Principles And Patterns."

Quotes:
- "Many client specific interfaces are better than one general purpose
interface"
"""


from abc import ABC, abstractmethod
from collections import OrderedDict, namedtuple

Display = namedtuple("Display", ["size", "ppi"])


class EBookReader(ABC):
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

    @abstractmethod
    def print(self, from_page: int, to_page: int) -> None:
        """Print one or more pages from the e-book.

        Args:
            from_page: The page to start printing from (inclusive).
            to_page: The last page that should be printed (inclusive).
        """
        raise NotImplementedError

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

    @abstractmethod
    def play_sound(self) -> None:
        """Play the sound on the current page."""
        raise NotImplementedError

    @abstractmethod
    def play_video(self) -> None:
        """Play the video on the current page."""
        raise NotImplementedError

    def add_bookmark(self) -> None:
        """Add a bookmark to the current page."""
        self._bookmarks.add(self._current_page)


# Reality: ComicBookReader's do not support playing sound or video.
# This class is forced to implement the entire contract provided by
# EBookReader. Futhermore, API changes to play_sound or play_video
# will result in uneccessary changes to this class.
class ComicBookReader(EBookReader):
    """An e-reader device that is capable of reading comic books."""

    def play_sound(self) -> None:
        """Play the sound on the current page."""
        raise NotImplementedError

    def play_video(self) -> None:
        """Play the video on the current page."""
        raise NotImplementedError

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

    kindle_reader = KindleReader(Display(size=6, ppi=167), storage_size=4)
