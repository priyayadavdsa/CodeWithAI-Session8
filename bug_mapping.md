# Bug to Test Mapping

| Bug | Class | Where | Test that exposed it | Failure seen |
|---|---|---|---|---|
| 1 | Arithmetic | calculate_average divided by len(prices) - 1 | test_average_of_three_prices | 300.0 != 200.0 |
| 1 | Arithmetic | same bug, second symptom | test_average_of_single_price | ZeroDivisionError |
| 2 | Boundary | is_eligible_for_discount used > instead of >= | test_eligible_exactly_at_minimum | False != True |
| 3 | Unreachable branch | get_discount_band checked >= 1000 before >= 2000 | test_gold_band | 'Silver' != 'Gold' |

One arithmetic bug produced two failing tests.
The other 5 tests passed on the buggy code, which is correct because those inputs were not affected by the bugs.