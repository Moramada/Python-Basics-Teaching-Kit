# ==============================================================================
# Lesson: Inheritance & Method Overriding (الوراثة وإعادة كتابة الدوال)
# ==============================================================================
# Inheritance = إنشاء كلاس جديد (Child Class) يرث جميع الصفات والدوال
# من كلاس آخر موجود بالفعل (Parent Class) لتجنب تكرار الكود.

# ----------------------------------------------------------
# 1. مثال الثلاجة الذكية (Fridge Hierarchy)
# ----------------------------------------------------------

class Fridge:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"The {self.brand} fridge is now ON and cooling.")

    def turn_off(self):
        self.is_on = False
        print(f"The {self.brand} fridge is now OFF.")


# كلاس الثلاجة الذكية (يرث من الكلاس الأساسي Fridge)
class SmartFridge(Fridge):
    def __init__(self, brand, color):
        # استدعاء constructor الكلاس الأساسي
        super().__init__(brand, color)
        self.wifi = True

    # دالة إضافية خاصة بالثلاجة الذكية
    def connect_wifi(self):
        print(f"Connecting {self.brand} smart fridge to Wi-Fi...")


# ----------------------------------------------------------
# 2. مثال السيارات والسيارة الكهربائية (Method Overriding)
# ----------------------------------------------------------

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def drive(self):
        print(f"The {self.brand} is driving using fuel.")

    def display_info(self):
        print(f"Brand: {self.brand}, Price: {self.price} EGP")


# كلاس السيارة الكهربائية (يقوم بإعادة كتابة دالة drive)
class ElectricCar(Car):
    def __init__(self, brand, price, battery_capacity):
        super().__init__(brand, price)
        self.battery_capacity = battery_capacity

    # Method Overriding (تعديل السلوك للكلاس الفرعي)
    def drive(self):
        print(f"The {self.brand} is driving silently using electricity.")

    # Extension Method (دالة جديدة بالكامل)
    def charge(self):
        print(f"Charging the {self.battery_capacity} kWh battery...")


# --- التجربة والاستدعاء ---
print("--- 1. اختبار وراثة الثلاجات ---")
smart_fridge = SmartFridge("Samsung", "Silver")
smart_fridge.turn_on()
smart_fridge.connect_wifi()

print("\n--- 2. اختبار وراثة السيارات الكهربائية ---")
tesla = ElectricCar("Tesla", 1500000, 75)
tesla.display_info()
tesla.drive()
tesla.charge()