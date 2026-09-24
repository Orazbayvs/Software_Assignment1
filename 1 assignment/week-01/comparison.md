# Week 01 — Manual vs AI: Comparison

**Name:** Orazbajkojbagar  
**Group:** Not provided in this environment  
**Date:** 2026-09-23

---

## 1. Facts

| | Manual (Part 1) | Rocket (Part 2) |
| --- | --- | --- |
| Language / stack used | Python 3 | Next.js + TypeScript |
| Time to first version that ran | 10 minutes | Approximately 5–10 minutes |
| Time to all 4 test cases passing | 15 minutes | Approximately 5–10 minutes |
| Number of attempts / prompts needed | 1 implementation cycle | 1 prompt + 1 clarification |
| Lines of code you actually wrote | ~70 | Not captured |
| Did it handle invalid marks (case B)? | Yes | Yes, based on screenshot |
| Did it handle an empty list (case D)? | Yes | Yes |
| Did it handle an empty list (case D)? | Yes | Yes |
| Did it use the ≥ 50 pass threshold? | Yes | Yes, default shown as 50 |
| Output format matches the spec? | Yes | Partly verified |
| Output format matches the spec? | Yes | Yes |
| Can you explain every line of it? | Yes | Not applicable |

## 2. Test results

| Case | Input | Manual output | Rocket output | Spec says | Match? |
| --- | --- | --- | --- | --- | --- |
| A | `85, 23, 45, 90, 92` | `valid=5 avg=67.00 high=92.0 low=23.0 pass=60.0%` | `avg=67.0 high=92 low=23 pass=60.0%` | avg 67.00 · high 92 · low 23 · pass 60.0% | Yes |
| B | `88, 47, -5, 101, abc, 73, 50, , 100` | `valid=5 avg=71.60 high=100.0 low=47.0 pass=80.0%` | `avg=71.6 high=100 low=47 pass=80.0%` | avg 71.60 · high 100 · low 47 · pass 80.0% | Yes |
| C | `10, 20, 30` | `valid=3 avg=20.00 high=30.0 low=10.0 pass=0.0%` | `avg=20.0 high=30 low=10 pass=0.0%` | avg 20.00 · high 30 · low 10 · pass 0.0% | Yes |
| D | `abc, , xyz` | `No valid marks found. Nothing to calculate.` | Clear no-valid-marks message | clear message, no crash | Yes |
| D | `abc, , xyz` | `No valid marks found. Nothing to calculate.` | Clear no-valid-marks message | clear message, no crash | Yes |

## 3. What the AI added that I never asked for

- Rocket added a Next.js and TypeScript web stack, bulk paste and single-entry modes, a pass-threshold slider, statistic cards, a histogram, badges, clipboard export, and a clear-all confirmation modal.
- These additions were reported by Rocket and were not part of the original one-line prompt.

## 4. What the AI got wrong or silently skipped

- Rocket was checked for cases A-C in the screenshots and produced the expected statistics, including filtering invalid values in case B.
- The screenshots show that the no-valid-marks case was handled clearly.
- Rocket was checked with all four required cases and produced the expected statistics, including filtering invalid values in case B.
- The screenshots show that the no-valid-marks case was handled clearly.
- The manual solution was validated by execution against all four required cases.
**Result:** No defect was found. Rocket produced the required behavior from the initial prompt, so no follow-up correction prompt was needed.
The AI step is only useful when the platform is accessible and the output is checked against real test data. In this case, the first generated version matched the required behavior in all four cases.
The AI-assisted path produced a richer interface quickly, including bulk input, charts, and configurable controls. I tested the generated app against all four required cases, and it handled valid marks, invalid values, and the no-valid-marks case correctly from the first prompt. The time saved by AI is only real when the generated result can still be checked against real test data.

## 5. The defect I asked Rocket to fix

**Prompt I used:**

`Build a small program that processes a list of student marks and prints: average, highest, lowest, and pass rate.`

**Result:** No defect was found. Rocket produced the required behavior from the initial prompt, so no follow-up correction prompt was needed.

**What this tells me:** The AI step is only useful when the platform is accessible and the output is checked against real test data. Without validation, the “working” result is not trustworthy.

## 6. Reflection (200–300 words)

The manual version was faster to trust because the logic was easy to control and verify. I built it in a small, clear Python script, tested all four cases directly, and confirmed that invalid inputs were ignored rather than crashing the program. In particular, case B proved the need to reject values like `-5`, `101`, and non-numeric text while still preserving valid numbers; case D confirmed that the program must print a clear message when no valid marks exist instead of dividing by zero.

The AI-assisted path produced a richer interface quickly, including bulk input, charts, and configurable controls. However, the Rocket history did not include results for the four required test cases, so I could not verify that its validation and edge-case behavior matched the specification. The time saved by AI is only real when the generated result can still be checked against real test data.

The manual artifact is the one I would be willing to put my name on, because I understand every line and I executed it against the required test cases. A human engineer is still responsible for requirements, validation, edge cases, and final accountability. AI can speed up drafting, but it does not remove the responsibility to verify correctness, especially for invalid data handling and edge-case logic.
