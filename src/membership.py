import math
from src.database import add_user, get_user
from tabulate import tabulate


class Membership:

    BENEFITS = {
        "Platinum": {"discount": 0.15},
        "Gold": {"discount": 0.10},
        "Silver": {"discount": 0.08}
    }

    REQUIREMENTS = {
        "Platinum": (8, 15),
        "Gold": (6, 10),
        "Silver": (5, 7)
    }

    def __init__(self, username):
        self.username = username

    def show_benefit(self):
        table = []
        for tier, data in self.BENEFITS.items():
            table.append([tier, f"{data['discount']*100}%"])
        print(tabulate(table, headers=["Tier", "Discount"]))

    def show_requirements(self):
        table = []
        for tier, req in self.REQUIREMENTS.items():
            table.append([tier, req[0], req[1]])
        print(tabulate(table, headers=["Tier", "Expense", "Income"]))

    def add_new_user(self, username, tier, overwrite=False):
        if tier not in self.BENEFITS:
            raise ValueError("Invalid tier")
        add_user(username, tier, overwrite=overwrite)

    def predict_membership(self, expense, income):
        distances = {}

        for tier, (exp, inc) in self.REQUIREMENTS.items():
            d = math.sqrt((expense - exp)**2 + (income - inc)**2)
            distances[tier] = d

        result = min(distances, key=distances.get)

        # simpan ke JSON
        add_user(self.username, result, overwrite=True)

        return result

    def show_membership(self, username):
        return get_user(username)

    def calculate_price(self, username, prices):
        if not isinstance(prices, list):
            raise TypeError("prices must be list")

        tier = get_user(username)

        if tier is None:
            raise ValueError("User not found")

        discount = self.BENEFITS[tier]["discount"]
        total = sum(prices)

        return total * (1 - discount)