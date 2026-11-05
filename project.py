
# Student Daily Expense Tracker

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = [name, amount, category]
    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
    else:
        print("\n--- Your Expenses ---")

        for expense in expenses:
            print("Name:", expense[0])
            print("Amount: Rs.", expense[1])
            print("Category:", expense[2])
            print("-------------------")


def total_expense():
    total = 0

    for expense in expenses:
        total = total + expense[1]

    print("Total Expense: Rs.", total)


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")
