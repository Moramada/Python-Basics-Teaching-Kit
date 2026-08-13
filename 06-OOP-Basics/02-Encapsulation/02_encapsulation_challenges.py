# ==============================================================================
# Tasks: Encapsulation Challenges (تحديات مفهوم التغليف)
# ==============================================================================

# ----------------------------------------------------------
# Challenge 1: بطارية الموبايل (Smartphone Battery)
# ----------------------------------------------------------

class SmartphoneBattery:
    def __init__(self, brand):
        self.brand = brand          
        self.__battery = 50         # نسبة الشحن مخفية وتبدأ بـ 50%

    def get_battery(self):
        return self.__battery

    def charge(self, amount):
        if self.__battery + amount <= 100:
            self.__battery += amount
            print(f"Charged! Battery level: {self.__battery}%")
        else:
            print("Error: Battery cannot be more than 100%!")

    def use_phone(self, amount):
        if self.__battery - amount >= 0:
            self.__battery -= amount
            print(f"Used phone. Battery remaining: {self.__battery}%")
        else:
            print("Error: Battery empty! Please charge your phone.")


# ----------------------------------------------------------
# Challenge 2: التكييف الذكي (Smart AC)
# ----------------------------------------------------------

class SmartAC:
    def __init__(self, brand):
        self.brand = brand               
        self.__temperature = 22          # درجة الحرارة الافتراضية 22

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, new_temp):
        if 16 <= new_temp <= 30:
            self.__temperature = new_temp
            print(f"Temperature set to: {self.__temperature}°C")
        else:
            print("Error: Invalid temperature! AC range must be between 16°C and 30°C.")


# --- التجربة والتطبيق ---
print("--- 1. اختبار تحدي بطارية الموبايل ---")
phone = SmartphoneBattery("iPhone")
phone.charge(30)
phone.use_phone(40)
phone.charge(90)  # سيناريو مرفوض

print("\n--- 2. اختبار تحدي التكييف الذكي ---")
ac = SmartAC("Sharp")
ac.set_temperature(18)
ac.set_temperature(10)  # سيناريو مرفوض