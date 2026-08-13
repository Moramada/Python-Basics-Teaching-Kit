# ==============================================================================
# Topic: Object-Oriented Programming (OOP) - Car Management System
# Level: Foundational / Intermediate
# Description: Explaining Classes, __init__ constructor, self reference, methods, and attribute updates.
# ==============================================================================

# 1. Class Definition (Template)
class Car:
    def __init__(self, color, price, model):
        # Attributes
        self.color = color
        self.price = price
        self.model = model

    # 2. Methods
    def display_info(self):
        print(f"Car Model : {self.model}")
        print(f"Color     : {self.color}")
        print(f"Price     : {self.price:,.2f} EGP")
        print("-" * 25)

    def update_price(self, new_price):
        self.price = new_price
        print(f"Price updated to: {self.price:,.2f} EGP")

    def apply_discount(self, percent):
        discount = self.price * (percent / 100)
        self.price -= discount
        print(f"New price after {percent}% discount: {self.price:,.2f} EGP")


# 3. Object Instantiation & Interaction
bmw = Car("Red", 200000, 2012)
ford = Car("Black", 500000, 2016)
toyota = Car("White", 300000, 2018)

print("=== Car Information ===")
bmw.display_info()
ford.display_info()
toyota.display_info()

print("=== Updating BMW ===")
bmw.update_price(250000)
bmw.apply_discount(10)
bmw.display_info()