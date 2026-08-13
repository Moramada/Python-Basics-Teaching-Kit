# ==============================================================================
# Tasks: Polymorphism Challenges (تحديات تعدد الأشكال)
# ==============================================================================

# ----------------------------------------------------------
# Challenge 1: حساب أجرة المواصلات (Ride Fare Challenge)
# ----------------------------------------------------------

class TokTok:
    def calculate_fare(self, distance):
        return distance * 5


class Taxi:
    def calculate_fare(self, distance):
        return (distance * 8) + 10


class Microbus:
    def calculate_fare(self, distance):
        return 7


# ----------------------------------------------------------
# Challenge 2: حساب فواتير البيت (Utility Bills Challenge)
# ----------------------------------------------------------

class ElectricityBill:
    def calculate_bill(self, units):
        return units * 2


class WaterBill:
    def calculate_bill(self, units):
        return units * 1.5


class GasBill:
    def calculate_bill(self, units):
        return (units * 1) + 10


# --- كود التجربة والتطبيق ---
print("--- 1. اختبار حساب أجرة المواصلات (10 كم) ---")
ride1 = TokTok()
ride2 = Taxi()
ride3 = Microbus()

print("TokTok Fare:", ride1.calculate_fare(10), "EGP")
print("Taxi Fare:", ride2.calculate_fare(10), "EGP")
print("Microbus Fare:", ride3.calculate_fare(10), "EGP")


print("\n--- 2. اختبار حساب فواتير البيت (100 وحدة) ---")
elec1 = ElectricityBill()
water1 = WaterBill()
gas1 = GasBill()

print("Electricity Bill:", elec1.calculate_bill(100), "EGP")
print("Water Bill:", water1.calculate_bill(100), "EGP")
print("Gas Bill:", gas1.calculate_bill(100), "EGP")