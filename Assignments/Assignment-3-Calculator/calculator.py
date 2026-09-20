# SkillNexis Python Programming
# Week 3 - Assignment 3
# Calculator Class with Exception Handling

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


calculator = Calculator()

print("================================")
print("      CALCULATOR")
print("================================")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = calculator.add(num1, num2)
    elif choice == "2":
        result = calculator.subtract(num1, num2)
    elif choice == "3":
        result = calculator.multiply(num1, num2)
    elif choice == "4":
        result = calculator.divide(num1, num2)
    else:
        raise ValueError("Invalid choice.")

    print("Result:", result)

except ValueError as e:
    print("Error:", e)

except ZeroDivisionError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected error:", e)