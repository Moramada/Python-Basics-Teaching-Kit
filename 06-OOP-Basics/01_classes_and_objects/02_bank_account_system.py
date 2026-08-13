# ==============================================================================
# Topic: Object-Oriented Programming (OOP) - Bank Account Management
# Level: Foundational / Intermediate
# Description: Demonstrating state mutation, validation checks (insufficient balance), and encapsulation concepts.
# ==============================================================================

# 1. Class Definition
class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    # 2. Behavior Methods
    def display_info(self):
        print(f"Holder Name    : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : {self.balance:,.2f} EGP")
        print("-" * 25)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount:,.2f} EGP.")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew {amount:,.2f} EGP.")
        else:
            print("Transaction Failed: Insufficient balance!")


# 3. Object Instantiation & Execution
acc1 = BankAccount("Ahmed Ali", "100123", 50000)
acc2 = BankAccount("Sara Mohamed", "100456", 15000)

print("=== Initial Accounts Information ===")
acc1.display_info()
acc2.display_info()

print("=== Transactions on Ahmed's Account ===")
acc1.deposit(10000)
acc1.withdraw(20000)
acc1.display_info()

print("=== Transactions on Sara's Account ===")
acc2.withdraw(20000)  # Attempting to withdraw more than available balance
acc2.display_info()