import unittest
from shop_utils import calculate_average, is_eligible_for_discount, get_discount_band


class TestShopUtils(unittest.TestCase):

    def test_average_of_three_prices(self):
        self.assertEqual(calculate_average([100, 200, 300]), 200.0)

    def test_average_of_single_price(self):
        self.assertEqual(calculate_average([400]), 400.0)

    def test_eligible_clearly_above_minimum(self):
        self.assertEqual(is_eligible_for_discount(501), True)

    def test_eligible_exactly_at_minimum(self):
        self.assertEqual(is_eligible_for_discount(500), True)

    def test_not_eligible_just_below_minimum(self):
        self.assertEqual(is_eligible_for_discount(499), False)

    def test_gold_band(self):
        self.assertEqual(get_discount_band(2500), "Gold")

    def test_silver_band(self):
        self.assertEqual(get_discount_band(1500), "Silver")

    def test_bronze_band(self):
        self.assertEqual(get_discount_band(700), "Bronze")

    def test_no_band_below_all(self):
        self.assertEqual(get_discount_band(100), "None")

    def test_silver_exactly_at_boundary(self):
        self.assertEqual(get_discount_band(1000), "Silver")


unittest.main(argv=[""], exit=False)