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


class DatetimeParser:
    """A DatetimeParser object represents a configurable datetime parser."""

    def __init__(
        self, date_string: str, *, format: str, str_format: str
    ) -> None:  # noqa
        """Initializes a new DatetimeParser instance. All arguments are
        required.

        Args:
            date_string: A string representation of a date to parse.
            format: The format of the date_string.
            str_format: The format of the string representation for the parsed
            date_string.
        """
        if not date_string or not date_string.strip():
            raise ValueError("date_string should contain a date")
        if not format or not format.strip():
            raise ValueError("format should contain valid format codes")
        if not str_format or not str_format.strip():
            raise ValueError("str_format should contain valid format codes")

        self._date_string = date_string
        self.format = format
        self._str_format = str_format

    def parse(self) -> datetime:
        """Return a datetime object."""
        return datetime.strptime(self._date_string, self.format)

    def __str__(self) -> str:
        return self.parse().strftime(self._str_format)


def build_long_date_parser(date_string: str) -> DatetimeParser:
    """Return a DatetimeParser that formats the date_string as a long date string.

    Args:
        date_string: A string representation of a date to parse.
    """
    return DatetimeParser(date_string, format="%Y-%m-%d", str_format="%c")


def build_short_date_parser(date_string: str) -> DatetimeParser:
    """Return a DatetimeParser that formats the date_string as a short date string.

    Args:
        date_string: A string representation of a date to parse.
    """
    return DatetimeParser(date_string, format="%Y-%m-%d", str_format="%x")


# print_log_event is no longer dependent on a particular concrete
# implementation
def print_log_event(
    log_event: LogEvent, parse_date: Callable[[str], DatetimeParser] = None
) -> None:  # noqa
    """Print the log event to standard out.

    Args:
        log_event: The LogEvent to print.
        parse_date: If specified, will be called with every LogEvent date. By
        default, a parser with a long date format is used.
    """
    parse_date = parse_date or build_long_date_parser
    print(
        f"{parse_date(log_event.date)}: [{log_event.level}] {log_event.detail}"
    )  # noqa


log_lines = [
    LogEvent("INFO", "Loading module spam.", "2022-06-26"),
    LogEvent("INFO", "Loading module more_spam.", "2022-06-26"),
    LogEvent("WARNING", "Not enough spam.", "2022-06-26"),
    LogEvent("ERROR", "TypeError in module spam.", "2022-06-26"),
]

# The caller can control how dates are parsed and displayed
# and doesn't need to know the details of how to construct a
# DatetimeParser object.
for log_line in log_lines:
    print_log_event(log_line, parse_date=build_long_date_parser)

for log_line in log_lines:
    print_log_event(log_line, parse_date=build_short_date_parser)
