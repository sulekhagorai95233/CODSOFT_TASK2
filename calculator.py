def calculator():
    print("Welcome to the Simple Calculator!")

    # Prompt user to input the first number
    num1 = float(input("Enter the first number: "))

    # Prompt user to input the second number
    num2 = float(input("Enter the second number: "))

    # Display operation choices
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Prompt user to choose an operation
    choice = input("Enter choice (1/2/3/4): ")

    # Perform the calculation based on the user's choice
    if choice == '1':
        result = num1 + num2
        operation = "addition"
    elif choice == '2':
        result = num1 - num2
        operation = "subtraction"
    elif choice == '3':
        result = num1 * num2
        operation = "multiplication"
    elif choice == '4':
        if num2 != 0:  # Check for division by zero
            result = num1 / num2
            operation = "division"
        else:
            print("Error! Division by zero.")
            return
    else:
        print("Invalid input! Please enter a valid choice.")
        return

    # Display the result
    print(f"The result of the {operation} of {num1} and {num2} is: {result}")


# Run the calculator function
calculator()