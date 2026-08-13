# ==============================================================================
# Lesson: Polymorphism (تعدد الأشكال)
# ==============================================================================
# Polymorphism = استخدام نفس اسم الدالة مع كائنات مختلفة، 
# وكل كائن ينفذ الدالة بطريقته الخاصة والمناسبة لوظيفته.

# ----------------------------------------------------------
# 1. مثال حساب مرتبات الموظفين (Employee Salary)
# ----------------------------------------------------------

class FullTimeEmployee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


class FreelanceEmployee:
    def __init__(self, name, task_price):
        self.name = name
        self.task_price = task_price

    def calculate_salary(self):
        return self.task_price


# --- تطبيق الـ Polymorphism بشكل مباشر ---
print("--- 1. حساب مرتبات الموظفين ---")

emp1 = FullTimeEmployee("Ahmed", 10000)
emp2 = PartTimeEmployee("Mona", 50, 100)
emp3 = FreelanceEmployee("Ali", 3000)

print(emp1.name, "Salary:", emp1.calculate_salary(), "EGP")
print(emp2.name, "Salary:", emp2.calculate_salary(), "EGP")
print(emp3.name, "Salary:", emp3.calculate_salary(), "EGP")


# ----------------------------------------------------------
# 2. مثال وسائل الدفع في المتجر (Payment Methods)
# ----------------------------------------------------------

class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid {amount} EGP using Credit Card (Visa/Mastercard).")


class VodafoneCashPayment:
    def pay(self, amount):
        print(f"Paid {amount} EGP using Vodafone Cash Wallet.")


class CashOnDelivery:
    def pay(self, amount):
        print(f"Paid {amount} EGP Cash upon delivery.")


print("\n--- 2. طرق الدفع في المتجر ---")

payment1 = CreditCardPayment()
payment2 = VodafoneCashPayment()
payment3 = CashOnDelivery()

payment1.pay(500)
payment2.pay(150)
payment3.pay(1000)