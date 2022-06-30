# dip_solution_1.py
# !/usr/bin/env python3
"""The first solution.

Utilize Python's support for first class callables.

This problem is inspired by Brandon Rhodes examination of the AbstractFactory
pattern in Python: https://python-patterns.guide/gang-of-four/abstract-factory/
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Callable


@dataclass
class LogEvent:
    """Represents a single log event.

    Public attributes:
    - level: The level of the logged event (e.g. WARNING).
    - detail: The detail of logged event.
    - date: The date of when the logged event was recorded.
    """

    level: str
    detail: str
    date: str


class DateTimeParser:
    """A DateTimeParser object represents a configurable datetime parser."""

    def __init__(self, *, format: str, str_format: str) -> None:  # noqa
        """Initializes a new DateTimeParser instance. All arguments are
        required.

        Args:
            format: The format of the date_string.
            str_format: The format of the string representation for the parsed
            date_string.
        """
        if not format or not format.strip():
            raise ValueError("format should contain valid format codes")
        if not str_format or not str_format.strip():
            raise ValueError("str_format should contain valid format codes")

        self._format = format
        self._str_format = str_format

    def to_datetime(self, date_string: str) -> datetime:
        """Return a datetime object.

        Args:
            date_string: A string representation of a date to parse.
        """
        if not date_string or not date_string.strip():
            raise ValueError("date_string should contain a date")
        return datetime.strptime(date_string, self._format)

    def to_string(self, date_string: str) -> str:
        """Return a string representation based on str_format.

        Args:
            date_string: A string representation of a date to parse.
        """
        if not date_string or not date_string.strip():
            raise ValueError("date_string should contain a date")
        return self.to_datetime(date_string).strftime(self._str_format)


def build_long_date_parser() -> DateTimeParser:
    """Return a DateTimeParser that formats the date_string as a long date
    string."""
    return DateTimeParser(format="%Y-%m-%d", str_format="%c")


def build_short_date_parser() -> DateTimeParser:
    """Return a DateTimeParser that formats the date_string as a short date
    string."""
    return DateTimeParser(format="%Y-%m-%d", str_format="%x")


# print_log_event is no longer dependent on a particular concrete
# implementation
def print_log_event(
    log_event: LogEvent, parse_date: Callable[[], DateTimeParser] = None
) -> None:  # noqa
    """Print the log event to standard out.

    Args:
        log_event: The LogEvent to print.
        parse_date: If specified, will be called with every LogEvent date. By
        default, a parser with a long date format is used.
    """
    parse_date = parse_date or build_long_date_parser
    print(
        (
            f"{parse_date().to_string(log_event.date)}: [{log_event.level}] "
            f"{log_event.detail}"
        )
    )  # noqa


log_lines = [
    LogEvent("INFO", "Loading module spam.", "2022-06-26"),
    LogEvent("INFO", "Loading module more_spam.", "2022-06-26"),
    LogEvent("WARNING", "Not enough spam.", "2022-06-26"),
    LogEvent("ERROR", "TypeError in module spam.", "2022-06-26"),
]

# The caller can control how dates are parsed and displayed
# and doesn't need to know the details of how to construct a
# DateTimeParser object.
for log_line in log_lines:
    print_log_event(log_line, parse_date=build_long_date_parser)

for log_line in log_lines:
    print_log_event(log_line, parse_date=build_short_date_parser)
