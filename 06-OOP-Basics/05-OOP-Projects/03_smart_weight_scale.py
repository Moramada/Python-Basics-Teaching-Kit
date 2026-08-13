# ==============================================================================
# Project 3: Smart Weight Scale System (نظام الميزان الذكي)
# ==============================================================================
# Concepts: Encapsulation, Inheritance, Polymorphism

# 1. Base Class
class Scale:
    def __init__(self, item_name):
        self.item_name = item_name
        self.__net_weight = 0  # Encapsulated Net Weight

    def get_weight(self):
        return self.__net_weight

    def set_weight(self, new_weight):
        self.__net_weight = new_weight


# 2. Subclasses
class BagScale(Scale):
    def calculate_weight(self, gross_weight):
        net = gross_weight - 0.1  # Deduct 100g bag weight
        self.set_weight(net)


class BoxScale(Scale):
    def calculate_weight(self, gross_weight):
        net = gross_weight - 0.5  # Deduct 500g box weight
        self.set_weight(net)


# --- Execution ---
print("--- 1. Bag Scale Test ---")
item1 = BagScale("Apples Bag")
item1.calculate_weight(5)
print("Item:", item1.item_name)
print("Net Weight:", item1.get_weight(), "Kg")

print("\n--- 2. Box Scale Test ---")
item2 = BoxScale("Tomatoes Box")
item2.calculate_weight(5)
print("Item:", item2.item_name)
print("Net Weight:", item2.get_weight(), "Kg")