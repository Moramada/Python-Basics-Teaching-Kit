# ==============================================================================
# Task: Smart TV Inheritance Challenge (تحدي التلفزيون الذكي)
# ==============================================================================

# 1. الكلاس الأساسي (Base Class)
class TV:
    def __init__(self, brand, screen_size):
        self.brand = brand
        self.screen_size = screen_size

    def turn_on(self):
        print(f"The {self.brand} {self.screen_size}-inch TV is ON (Cable Channels).")


# 2. الكلاس الفرعي (Derived Class)
class SmartTV(TV):
    def __init__(self, brand, screen_size):
        # استخدام super() للوراثة من الكلاس الأب
        super().__init__(brand, screen_size)

    def open_youtube(self):
        print(f"Opening YouTube on your {self.brand} Smart TV...")


# --- التجربة والاستدعاء ---
print("--- اختبار تطبيق الشاشة الذكية ---")
my_tv = SmartTV("Samsung", 55)
my_tv.turn_on()
my_tv.open_youtube()