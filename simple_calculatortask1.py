def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Welcome to the simple calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter your choice (1/2/3/4): ")
    
    if operation == '1':
        print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
    elif operation == '2':
        print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")
    elif operation == '3':
        print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")
    elif operation == '4':
        print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")
    else:
        print("Invalid input! Please enter a valid operation.")

# Run the calculator
calculator()
