# ==============================================================================
# Project 1: Smart Travel Card System (نظام كارت المواصلات الذكي)
# ==============================================================================
# Concepts: Encapsulation, Inheritance, Polymorphism

# 1. Base Class (Encapsulation)
class TravelCard:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.__balance = balance  # Private Attribute

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance


# 2. Derived Classes (Inheritance & Polymorphism)
class StudentCard(TravelCard):
    def pay_trip(self):
        cost = 2  # Student rate
        current = self.get_balance()
        self.set_balance(current - cost)
        print(f"Student Trip Paid: {cost} EGP")


class AdultCard(TravelCard):
    def pay_trip(self):
        cost = 6  # Standard rate
        current = self.get_balance()
        self.set_balance(current - cost)
        print(f"Adult Trip Paid: {cost} EGP")


# --- Execution ---
print("--- 1. Testing Student Card ---")
card1 = StudentCard("Ali", 20)
print("Holder:", card1.holder_name)
print("Start Balance:", card1.get_balance(), "EGP")
card1.pay_trip()
print("Balance Now:", card1.get_balance(), "EGP")

print("\n--- 2. Testing Adult Card ---")
card2 = AdultCard("Omar", 20)
print("Holder:", card2.holder_name)
print("Start Balance:", card2.get_balance(), "EGP")
card2.pay_trip()
print("Balance Now:", card2.get_balance(), "EGP")