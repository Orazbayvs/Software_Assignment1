#!/usr/bin/env python3
"""Student marks statistics.

Rules:
- A valid mark is a number between 0 and 100 inclusive.
- Empty values, text values, negatives, and values above 100 are ignored.
- Pass threshold is >= 50.
- If there are no valid marks, print a clear message and exit cleanly.
"""

from __future__ import annotations

import sys
from typing import Iterable, List


TEST_CASES = {
    "A": "85, 23, 45, 90, 92",
    "B": "88, 47, -5, 101, abc, 73, 50, , 100",
    "C": "10, 20, 30",
    "D": "abc, , xyz",
}


def parse_marks(raw_input: str | list | tuple | None) -> List[float]:
    """Return only valid numeric marks in the range [0, 100]."""
    if raw_input is None:
        return []

    if isinstance(raw_input, str):
        items = [part.strip() for part in raw_input.split(",")]
    else:
        items = [str(part).strip() for part in raw_input]

    valid_marks: List[float] = []
    for item in items:
        if item == "":
            continue
        try:
            value = float(item)
        except ValueError:
            continue
        if 0 <= value <= 100:
            valid_marks.append(value)
    return valid_marks


def summarize_marks(marks: Iterable[float]) -> dict:
    numbers = list(marks)
    if not numbers:
        return {
            "valid": 0,
            "average": None,
            "highest": None,
            "lowest": None,
            "pass_rate": None,
        }

    valid_count = len(numbers)
    average = sum(numbers) / valid_count
    highest = max(numbers)
    lowest = min(numbers)
    passes = sum(1 for value in numbers if value >= 50)
    pass_rate = (passes / valid_count) * 100

    return {
        "valid": valid_count,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "pass_rate": pass_rate,
    }


def format_number(value: float | None, digits: int = 2) -> str:
    if value is None:
        return "-"
    return format(value, f".{digits}f")


def print_summary(raw_input: str | list | tuple | None) -> None:
    marks = parse_marks(raw_input)
    stats = summarize_marks(marks)

    if stats["average"] is None:
        print("No valid marks found. Nothing to calculate.")
        return

    print(f"Number of valid marks: {stats['valid']}")
    print(f"Average: {stats['average']:.2f}")
    print(f"Highest: {stats['highest']}")
    print(f"Lowest: {stats['lowest']}")
    print(f"Pass rate: {stats['pass_rate']:.1f}%")


def main() -> None:
    if len(sys.argv) > 1:
        arg = sys.argv[1].upper()
        if arg in TEST_CASES:
            print_summary(TEST_CASES[arg])
            return
        if arg == "ALL":
            for case_name, case_input in TEST_CASES.items():
                print(f"\nCase {case_name}: {case_input}")
                print_summary(case_input)
            return

    print("Usage: python marks_stats.py [A|B|C|D|ALL]")
    print("Default example: A")
    print_summary(TEST_CASES["A"])


if __name__ == "__main__":
    main()
