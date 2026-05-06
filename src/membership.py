from tabulate import tabulate
from src.database import add_user, get_user

class Membership:

    _BENEFIT_DATA = [
        ["Silver", "8%", "Voucher Makanan"],
        ["Gold", "10%", "Benefit Silver + Voucher Ojek Online"],
        ["Platinum", "15%", "Benefit Gold + Voucher Liburan"]
    ]

    _REQUIREMENT_DATA = [
        ["Silver", "5 Juta", "7 Juta"],
        ["Gold", "6 Juta", "10 Juta"],
        ["Platinum", "8 Juta", "15 Juta"]
    ]

    _DISCOUNT = {
        "Silver": 0.08,
        "Gold": 0.10,
        "Platinum": 0.15
    }

    _TIER_PARAMS = {
        "Silver": {"monthly_spending": 5000000, "monthly_income": 7000000},
        "Gold": {"monthly_spending": 6000000, "monthly_income": 10000000},
        "Platinum": {"monthly_spending": 8000000, "monthly_income": 15000000}
    }

    def __init__(self, username):
        self.username = username

    def show_benefits(self):
        benefits = tabulate(self._BENEFIT_DATA, headers = ["Tier", "Discount", "Another Benefit"])
        print(benefits)
    def show_requirements(self):
        pass
    def add_new_user(self, username, tier):
        add_user(username, tier)
        print(f"User {username} berhasil ditambahkan dengan tier {tier}")
    def show_membership(self):
        pass
    def predit_tier(self, monthly_spending, monthly_income):
        # \(d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2})
        distances = {}

        for tier, params in self._TIER_PARAMS.items():
            monthly_spending_param = params['monthly_spending']
            monthly_income_param = params['monthly_income']

            distance = ((monthly_spending - monthly_spending_param)**2+(monthly_income - monthly_income_param)**2)**0.5
            distances[tier] = distance
        predicted_tier = min(distances, key=distances.get)
        print(f"Predicted Tier: {predicted_tier}")
        return predicted_tier
    def calculate_price(self, username, list_harga):
        tier = get_user(username)
        if tier is None:
            print(f"User {username} tidak ditemukan")
            return None
        discount = self._DISCOUNT.get(tier, 0)
        total_price = sum(list_harga)
        discounted_price = total_price * (1-discount)
        print(f"{username} dengan tier {tier} mendapatkan diskon {discount*100}% Total harga setelah diskon: {discounted_price}")