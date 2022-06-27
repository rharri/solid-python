# dependency_inversion_principle.py
# !/usr/bin/env python3
"""A demonstration of the dependency inversion principle

This demonstration is based on Robert C. Martin's paper titled,
"Design Principles And Patterns."

Quotes:
- "Depend upon Abstractions. Do not depend upon concretions."
- " ... concrete things change alot, abstract things change much
less frequently."
- "The DIP makes the assumption that anything concrete is volatile."
- "One of the most common places that designs depend upon concrete classes is
when those designs create instances ... there is an elegant solution to this
problem named AbstractFactory."

This problem is inspired by Brandon Rhodes examination of the AbstractFactory
pattern in Python: https://python-patterns.guide/gang-of-four/abstract-factory/
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class LogLine:
    """Represents a log line."""

    level: str
    detail: str
    date: str


# print_log is dependent on the concrete implementation of parse_long_date
def print_log(line: LogLine) -> None:
    """Print the log line to standard out."""

    def parse_long_date(value: str) -> str:
        """Format the value as a long date string."""
        dt = datetime.strptime(value, "%Y-%m-%d")
        return dt.strftime("%c")

    print(f"{parse_long_date(line.date)}: [{line.level}] {line.detail}")


log_lines = [
    LogLine("INFO", "Loading module spam.", "2022-06-26"),
    LogLine("INFO", "Loading module more_spam.", "2022-06-26"),
    LogLine("WARNING", "Not enough spam.", "2022-06-26"),
    LogLine("ERROR", "TypeError in module spam.", "2022-06-26"),
]

for log_line in log_lines:
    print_log(log_line)
