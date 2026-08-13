# ==============================================================================
# Final Capstone Project: Smart Mobile Line System
# ==============================================================================
# Unifying Classes, Encapsulation, Inheritance, and Polymorphism.

# 1. Base Class (Encapsulation)
class PhoneLine:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.__balance = balance  # Private Balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance


# 2. Derived Classes (Inheritance & Polymorphism)
class PrepaidLine(PhoneLine):
    def make_call(self, minutes):
        cost = minutes * 0.5  # 0.5 EGP per minute
        current = self.get_balance()
        self.set_balance(current - cost)
        print(f"Call duration: {minutes} mins | Cost: {cost} EGP")


class PostpaidLine(PhoneLine):
    def make_call(self, minutes):
        cost = minutes * 0.25  # 0.25 EGP per minute
        current = self.get_balance()
        self.set_balance(current - cost)
        print(f"Call duration: {minutes} mins | Cost: {cost} EGP")


# --- Execution & Final Evaluation ---
print("=== Capstone Project: Mobile Line System ===")

print("\n--- 1. Prepaid Line Execution ---")
line1 = PrepaidLine("Ahmed", 50)
print("Owner:", line1.owner_name)
print("Start Balance:", line1.get_balance(), "EGP")
line1.make_call(10)
print("Balance Now:", line1.get_balance(), "EGP")

print("\n--- 2. Postpaid Line Execution ---")
line2 = PostpaidLine("Mona", 50)
print("Owner:", line2.owner_name)
print("Start Balance:", line2.get_balance(), "EGP")
line2.make_call(10)
print("Balance Now:", line2.get_balance(), "EGP")