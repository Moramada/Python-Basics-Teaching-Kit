# ==============================================================================
# Topic: Conditional Statements (If / Elif / Else)
# Level: Foundational
# Description: Control flow logic using academic evaluation and basic calculator.
# ==============================================================================

# Example 1: Student Academic Evaluation
name = input("Enter your name: ")
level = int(input("Enter your level: "))
exam_grade = float(input("Enter your grade: "))

if exam_grade >= 90:
    print("Your Academic Evaluation Is Excellent")
elif exam_grade >= 80:
    print("Your Academic Evaluation Is Very Good")
elif exam_grade >= 70:
    print("Your Academic Evaluation Is Good")
elif exam_grade >= 60:
    print("Your Academic Evaluation Is Weak")
elif exam_grade >= 50:
    print("Your Academic Evaluation Is Pass")
else:
    print("Unfortunately, you did not pass.")

print("-" * 40)

# Example 2: Simple Calculator using Operators
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, ^): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
elif operator == "^":
    print("Result:", num1 ** num2)
else:
    print("Error: Invalid Operator")