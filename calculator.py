def calculator():
    # Get input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ").strip()
    
    # Perform the operation based on user input
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        result = num1 / num2
    else:
        return "Error: Invalid operation. Please use +, -, *, or /"
    
    return f"{num1} {operation} {num2} = {result}"

# Run the calculator
print("Simple Calculator")
print("----------------")
print(calculator())