def calculator():
    while True:
        print("\nSimple Calculator")
        print("Enter two numbers:")
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            operation = input("Choose operation (+, -, *, /) or 'q' to quit: ")

            if operation == "+":
                print(f"Result: {num1 + num2}")
            elif operation == "-":
                print(f"Result: {num1 - num2}")
            elif operation == "*":
                print(f"Result: {num1 * num2}")
            elif operation == "/":
                print(f"Result: {num1 / num2 if num2 != 0 else 'Error: Division by zero!'}")
            elif operation == "q":
                print("Exiting calculator...")
                break
            else:
                print("Invalid operation! Try again.")
        except ValueError:
            print("Invalid input! Please enter numbers.")

if __name__ == "__main__":
    calculator()
