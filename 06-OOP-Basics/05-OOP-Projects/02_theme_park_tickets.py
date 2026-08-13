# ==============================================================================
# Project 2: Theme Park Tickets System (نظام تذاكر الملاهي)
# ==============================================================================
# Concepts: Encapsulation, Inheritance, Polymorphism

# 1. Base Class
class ParkTicket:
    def __init__(self, visitor_name):
        self.visitor_name = visitor_name
        self.__price = 0  # Encapsulated Price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price


# 2. Subclasses
class ChildTicket(ParkTicket):
    def calculate_price(self, base_price):
        final_price = base_price / 2
        self.set_price(final_price)


class AdultTicket(ParkTicket):
    def calculate_price(self, base_price):
        final_price = base_price + 20
        self.set_price(final_price)


# --- Execution ---
print("--- 1. Child Ticket Test ---")
t1 = ChildTicket("Ahmed")
t1.calculate_price(100)
print("Visitor:", t1.visitor_name)
print("Ticket Price:", t1.get_price(), "EGP")

print("\n--- 2. Adult Ticket Test ---")
t2 = AdultTicket("Mahmoud")
t2.calculate_price(100)
print("Visitor:", t2.visitor_name)
print("Ticket Price:", t2.get_price(), "EGP")