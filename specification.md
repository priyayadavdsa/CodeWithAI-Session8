# Specification: shop_utils

| Function call | Must return | What it tests |
|---|---|---|
| calculate_average([100, 200, 300]) | 200.0 | Ordinary arithmetic |
| calculate_average([400]) | 400.0 | Single element, no crash |
| is_eligible_for_discount(501) | True | Clearly above minimum |
| is_eligible_for_discount(500) | True | Exactly at minimum |
| is_eligible_for_discount(499) | False | Just below minimum |
| get_discount_band(2500) | "Gold" | Top band |
| get_discount_band(1500) | "Silver" | Middle band |
| get_discount_band(700) | "Bronze" | Lowest band |
| get_discount_band(100) | "None" | Below all bands |