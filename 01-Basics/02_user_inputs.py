# ==============================================================================
# Topic: User Inputs & Type Casting
# Level: Foundational
# Description: Handling user inputs, string concatenation, and numeric casting.
# ==============================================================================

# 1. String Input & Greeting
name = input("Enter your name: ")
print("Welcome my friend,", name)

# 2. Input with Data Type Casting (Simple Calculator)
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")

# Converting inputs from String to Float before addition
result = float(num1) + float(num2)
print("Result of addition:", result)