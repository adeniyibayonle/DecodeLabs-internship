total = 0

print("Expense Tracker")
print("Type 'quit' to stop\n")

while True:

    user_input = input("Enter expense: ")

    if user_input.lower() == "quit":

        print(f"\nFinal Total: ${total:.2f}")
        break

    try:

        expense = float(user_input)

        total += expense

        print(f"Current Total: ${total:.2f}")

    except ValueError:

        print("Please enter a valid number.")