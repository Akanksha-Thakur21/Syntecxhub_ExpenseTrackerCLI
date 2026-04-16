import csv
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"


# Initialize file
def init_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])
    except FileExistsError:
        pass


# Add expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print(" Invalid amount!\n")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense added!\n")


# View expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\n All Expenses:")
            for row in reader:
                print(row)
        print()
    except FileNotFoundError:
        print("No data found.\n")


# Monthly summary
def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if row[0].startswith(month):
                    total += float(row[2])

        print(f"\nTotal for {month}: {total}\n")
    except:
        print("No data available.\n")


# Category summary
def category_summary():
    summary = defaultdict(float)

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                summary[row[1]] += float(row[2])

        print("\nCategory Summary:")
        for cat, amt in summary.items():
            print(f"{cat}: {amt}")
        print()
    except:
        print("No data available.\n")


# Export to CSV (copy file)
def export_data():
    export_file = "exported_expenses.csv"

    try:
        with open(FILE_NAME, "r") as src, open(export_file, "w", newline="") as dst:
            dst.write(src.read())

        print(f"Exported to {export_file}\n")
    except:
        print("No data to export.\n")


# Generate chart
def generate_chart():
    summary = defaultdict(float)

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                summary[row[1]] += float(row[2])

        categories = list(summary.keys())
        amounts = list(summary.values())

        plt.bar(categories, amounts)
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.title("Expense Chart")
        plt.show()

    except:
        print("No data to plot.\n")


# Main menu
def menu():
    init_file()

    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Export to CSV")
        print("6. Show Chart")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            export_data()
        elif choice == "6":
            generate_chart()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")


menu()