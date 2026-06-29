import csv

filename = "expenses.csv"

def add_expense():
    item = input("Expense Name: ")
    amount = input("Amount: ")

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item, amount])

    print("Expense Added Successfully!")

def view_expenses():
    print("\nExpenses")
    print("---------------------")

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            total = 0

            for row in reader:
                print(f"{row[0]} - ₹{row[1]}")
                total += float(row[1])

            print("---------------------")
            print("Total Expense = ₹", total)

    except FileNotFoundError:
        print("No expenses found.")

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        break

    else:
        print("Invalid Choice")
