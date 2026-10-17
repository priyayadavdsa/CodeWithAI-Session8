import unittest

from shop_utils import (
    MIN_BILL,
    calculate_average,
    get_discount_band,
    is_eligible_for_discount,
)


class TestCalculateAverage(unittest.TestCase):
    # NOTE: calculate_average divides by len(prices) - 1 instead of len(prices),
    # so the tests below that expect a correct average will FAIL until it is fixed.

    def test_average_of_multiple_prices_returns_mean(self):
        self.assertAlmostEqual(calculate_average([100, 200, 300]), 200)

    def test_average_of_single_price_returns_that_price(self):
        self.assertAlmostEqual(calculate_average([400]), 400)

    def test_average_of_two_prices_returns_mean(self):
        self.assertAlmostEqual(calculate_average([10, 20]), 15)

    def test_average_of_float_prices_returns_float_mean(self):
        self.assertAlmostEqual(calculate_average([10.5, 20.5]), 15.5)

    def test_average_of_empty_list_raises_error(self):
        with self.assertRaises((ZeroDivisionError, ValueError)):
            calculate_average([])


class TestIsEligibleForDiscount(unittest.TestCase):
    def test_bill_above_minimum_is_eligible(self):
        self.assertTrue(is_eligible_for_discount(MIN_BILL + 1))

    def test_bill_below_minimum_is_not_eligible(self):
        self.assertFalse(is_eligible_for_discount(MIN_BILL - 1))

    def test_bill_exactly_at_minimum_is_eligible(self):
        # NOTE: the function uses ">" so this FAILS if the minimum is meant to be inclusive.
        self.assertTrue(is_eligible_for_discount(MIN_BILL))

    def test_zero_bill_is_not_eligible(self):
        self.assertFalse(is_eligible_for_discount(0))

    def test_returns_boolean_type(self):
        self.assertIsInstance(is_eligible_for_discount(1000), bool)


class TestGetDiscountBand(unittest.TestCase):
    # NOTE: the "Silver" check (>= 1000) comes before the "Gold" check (>= 2000),
    # so Gold is unreachable and the Gold tests below will FAIL until the order is fixed.

    def test_bill_of_2500_returns_gold(self):
        self.assertEqual(get_discount_band(2500), "Gold")

    def test_bill_exactly_2000_returns_gold(self):
        self.assertEqual(get_discount_band(2000), "Gold")

    def test_bill_of_1500_returns_silver(self):
        self.assertEqual(get_discount_band(1500), "Silver")

    def test_bill_exactly_1000_returns_silver(self):
        self.assertEqual(get_discount_band(1000), "Silver")

    def test_bill_just_below_1000_returns_bronze(self):
        self.assertEqual(get_discount_band(999), "Bronze")

    def test_bill_of_700_returns_bronze(self):
        self.assertEqual(get_discount_band(700), "Bronze")

    def test_bill_exactly_at_minimum_returns_bronze(self):
        self.assertEqual(get_discount_band(MIN_BILL), "Bronze")

    def test_bill_just_below_minimum_returns_none_band(self):
        self.assertEqual(get_discount_band(MIN_BILL - 1), "None")

    def test_bill_of_100_returns_none_band(self):
        self.assertEqual(get_discount_band(100), "None")

    def test_zero_bill_returns_none_band(self):
        self.assertEqual(get_discount_band(0), "None")


class TestModuleConstants(unittest.TestCase):
    def test_min_bill_is_500(self):
        self.assertEqual(MIN_BILL, 500)


if __name__ == "__main__":
    unittest.main()