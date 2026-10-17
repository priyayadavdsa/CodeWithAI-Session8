def calculate_average(prices):
    total = 0
    for p in prices:
        total = total + p
    return total / len(prices)

MIN_BILL = 500

def is_eligible_for_discount(bill):
    if bill >= MIN_BILL:
        return True
    return False

def get_discount_band(bill):
    if bill >= 2000:
        return "Gold"
    elif bill >= 1000:
        return "Silver"
    elif bill >= MIN_BILL:
        return "Bronze"
    return "None"

if __name__ == "__main__":
    print(calculate_average([100, 200, 300]))
    print(calculate_average([400]))
    print(is_eligible_for_discount(500))
    print(is_eligible_for_discount(499))
    print(get_discount_band(2500))
    print(get_discount_band(1500))
    print(get_discount_band(700))
    print(get_discount_band(100))