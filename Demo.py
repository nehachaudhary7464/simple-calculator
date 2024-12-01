# Simple Calculator
print("Welcome to the Simple Calculator!")
print("Choose an operation: +, -, *, /")

# Get user input
operation = input("Enter the operation: ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "undefined (division by zero is not allowed)"
else:
    result = "Invalid operation"

# Display the result
print(f"The result is: {result}")
