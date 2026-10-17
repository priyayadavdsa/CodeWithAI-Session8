# Session 8: Red Before Green

A small shop billing module (`shop_utils.py`) with three functions:
`calculate_average`, `is_eligible_for_discount` and `get_discount_band`.

## Testing

**Run command:**

    python test_shop_utils.py

**Specification:** `specification.md` has 10 rows (9 original + 1 student-designed boundary row).

**Spec-based tests:** `test_shop_utils.py` has 10 tests. The first 9 were written from the specification before any fix (RED commit `d95f64f`). The 10th is a student-designed boundary test added after the green stage (commit `66292fd`).

**Red stage:** on the buggy code, 9 tests ran and 4 failed (3 failures, 1 error). Evidence: `red_output.txt`, commit `d95f64f`.

**Green stage:** after fixing three bugs, the same 9 tests passed. Evidence: `green_output.txt`, commit `5f27d9a`.

**Bugs found:**

| Bug | Class | Test that exposed it |
|---|---|---|
| 1 | Arithmetic (`len(prices) - 1`) | test_average_of_three_prices, test_average_of_single_price |
| 2 | Boundary (`>` instead of `>=`) | test_eligible_exactly_at_minimum |
| 3 | Unreachable branch (Silver checked before Gold) | test_gold_band |

**Experiment (tests generated from buggy code):**
- AI-generated tests are in `test_generated.py` (21 tests).
- On the buggy code: 7 failures and 1 error (`generated_buggy_output.txt`).
- On the fixed code: all 21 passed (`generated_fixed_output.txt`).
- Result: in this experiment the AI noticed the bugs while reading the code and wrote tests with the correct expected behaviour, so its tests caught all 3 bugs. This was not the "trap" outcome, and I am reporting it as it happened.