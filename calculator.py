def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("Simple Calculator")
    
    while True:
        print("\nOptions: + (Add), - (Subtract), * (Multiply), / (Divide), q (Quit)")
        choice = input("Enter operation: ")

        if choice == "q":
            print("Goodbye!")
            break

        if choice in ["+", "-", "*", "/"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "+":
                    print("Result:", add(num1, num2))
                elif choice == "-":
                    print("Result:", subtract(num1, num2))
                elif choice == "*":
                    print("Result:", multiply(num1, num2))
                elif choice == "/":
                    print("Result:", divide(num1, num2))

            except ValueError:
                print("Invalid input! Please enter numbers.")

        else:
            print("Invalid operation! Try again.")

        # Ask user if they want to continue
        exit_choice = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if exit_choice != "yes":
            print("Exiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
