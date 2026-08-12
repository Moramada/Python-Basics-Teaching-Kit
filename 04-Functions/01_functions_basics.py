# ==============================================================================
# Topic: Functions Basics, Parameters, & Return Values
# Level: Foundational
# Description: Explaining function definition, parameters, arguments, return statements, and default values.
# ==============================================================================

# 1. Basic Function without Parameters
print("--- 1. Simple Function ---")
def greet_user():
    print("Welcome to the Python Course!")

# Calling the function
greet_user()

# 2. Function with Parameters (Passing Data)
print("\n--- 2. Function with Parameters ---")
def welcome_student(name, course_name):
    print(f"Hello {name}, welcome to {course_name} class!")

welcome_student("Ahmed", "Python Basics")
welcome_student("Sara", "Data Science")

# 3. Function with Default Parameters
print("\n--- 3. Function with Default Parameters ---")
def calculate_price(item_name, price, tax_rate=0.14):
    total = price + (price * tax_rate)
    print(f"Item: {item_name} | Final Price with Tax: {total}")

calculate_price("Laptop", 10000)        # Uses default tax_rate (0.14)
calculate_price("Phone", 5000, 0.10)   # Overrides default tax_rate

# 4. Function with Return Statement
print("\n--- 4. Function Returning Values ---")
def add_numbers(num1, num2):
    result = num1 + num2
    return result

# Storing the returned value in a variable
sum_result = add_numbers(15, 25)
print("The calculated sum is:", sum_result)

# 5. Using Return Values in Logic
print("\n--- 5. Practical Example: Pass/Fail Evaluation ---")
def check_grade(score):
    if score >= 50:
        return "Passed"
    else:
        return "Failed"

student_status = check_grade(75)
print("Student Status:", student_status)