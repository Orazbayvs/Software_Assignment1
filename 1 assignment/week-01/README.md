# Manual solution for student marks statistics

This solution is written in Python and handles invalid input safely.

## Run

From the project root:

```bash
python3 week-01/manual/marks_stats.py A
python3 week-01/manual/marks_stats.py B
python3 week-01/manual/marks_stats.py C
python3 week-01/manual/marks_stats.py D
python3 week-01/manual/marks_stats.py ALL
```

## What it does

- Ignores empty values, text, negative values, and numbers outside [0, 100]
- Counts only valid marks
- Computes average, highest, lowest, and pass rate
- Prints a clear message when there are no valid marks

## Notes

The program accepts a built-in case selector (`A`, `B`, `C`, `D`, or `ALL`) for
testing.