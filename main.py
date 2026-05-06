from src.membership import Membership

membership = Membership("Sumbul")
membership.show_benefits()
membership.add_new_user("Devi", "Gold")
membership.predit_tier(8000000, 15000000)
membership.calculate_price("Devi", [50_000, 100_000, 200_000])