def calculator():
    print("Simple Calculator")
    print("-----------------")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("-----------------")
    
    try:
        #  Now we are getting user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ").strip()
        
        # Perform calculations based on selected operation
        if operation == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid operation! Please choose from +, -, *, /")
    
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")


while True:
    calculator()
    another = input("\nDo you want to perform another calculation? (yes/no): ").lower()
    if another != 'yes':
        print("Goodbye!")
        break
    print()