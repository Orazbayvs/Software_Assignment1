# Rocket AI Prompt Log — Week 01

## 1. Initial Prompt

> Build a small program that processes a list of student marks and prints:
> average, highest, lowest, and pass rate.

## 2. Requirements Elicitation & Rewritten Prompt

- **Prompt Score:** Initial 79% -> Final 84%
- **Clarification Question Asked by Rocket:** "Who will be using this tool to enter and view the student marks?"
- **My Answer:** "Just me, for personal use (A personal tool to quickly crunch marks locally)"

### Rocket Enhanced Prompt

> A personal student marks calculator that lets me input a list of marks and instantly computes the average, highest score, lowest score, and pass rate — all displayed cleanly in one view.
>
> Building with Next.js and TypeScript.

## 3. What Rocket Added Unprompted

- Next.js and TypeScript web stack.
- One-by-one and bulk paste input modes.
- Configurable pass threshold slider.
- Six live statistic cards: average, highest, lowest, pass rate, total count, and fail count.
- Recharts score distribution histogram with pass/fail coloring.
- Per-mark badges.
- Copy-stats-to-clipboard feature.
- Confirmation modal for clearing all marks.

## 4. Rocket Build Result

Rocket reported:

> Built MarksCalc Web App

## 5. Test Results

The app was tested with all four required cases after the initial prompt. It
produced the correct statistics, ignored invalid values, and handled the empty
valid-data case correctly.

- **Case A:** Average 67.0, highest 92, lowest 23, pass rate 60.0%.
- **Case B:** Average 71.6, highest 100, lowest 47, pass rate 80.0%; invalid
	values were ignored.
- **Case C:** Average 20.0, highest 30, lowest 10, pass rate 0.0%.
- **Case D:** Displayed a clear no-valid-marks message.

Rocket completed the required behavior correctly after the initial prompt. No
follow-up correction prompt was needed.
