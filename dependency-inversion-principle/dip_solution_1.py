# dip_solution_1.py
# !/usr/bin/env python3
"""The first solution.

Utilize Python's support for first class functions.

This problem is inspired by Brandon Rhodes examination of the AbstractFactory
pattern in Python: https://python-patterns.guide/gang-of-four/abstract-factory/
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Callable


@dataclass
class LogLine:
    """Represents a log line."""

    level: str
    detail: str
    date: str


class DateParser:
    """A flexible date parser."""

    def __init__(self, value: str, in_fmt: str, out_fmt: str) -> None:
        self.value = value
        self.in_fmt = in_fmt
        self.out_fmt = out_fmt

    def parse(self) -> datetime:
        return datetime.strptime(self.value, self.in_fmt)

    def __str__(self) -> str:
        return self.parse().strftime(self.out_fmt)


def build_long_date_parser(value: str) -> DateParser:
    """Construct a DateParser that formats the value as a long date string."""
    return DateParser(value, "%Y-%m-%d", "%c")


def build_short_date_parser(value: str) -> DateParser:
    """Construct a DateParser that formats the value as a short date string."""
    return DateParser(value, "%Y-%m-%d", "%x")


# print_log is no longer dependent on a particular concrete implementation
def print_log(
    line: LogLine, parse_date: Callable[[str], DateParser] = None
) -> None:  # noqa
    """Print the log line to standard IO."""
    parse_date = parse_date or build_long_date_parser
    print(f"{parse_date(line.date)}: [{line.level}] {line.detail}")


log_lines = [
    LogLine("INFO", "Loading module spam.", "2022-06-26"),
    LogLine("INFO", "Loading module more_spam.", "2022-06-26"),
    LogLine("WARNING", "Not enough spam.", "2022-06-26"),
    LogLine("ERROR", "TypeError in module spam.", "2022-06-26"),
]

# The caller can control how dates are parsed and displayed
# and doesn't need to know the details of how to construct a
# DateParser object.
for log_line in log_lines:
    print_log(log_line, parse_date=build_long_date_parser)

for log_line in log_lines:
    print_log(log_line, parse_date=build_short_date_parser)
