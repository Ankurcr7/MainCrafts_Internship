# Expense Tracker

import csv

def add_expense(desc: str, amount: float) -> None:
    try:
        f = open("expenses.csv", "a", newline="\n")
        writer = csv.writer(f)
        writer.writerow([desc, amount])

        print("Successfully Added!\n")

    except Exception:
        print("Unexpected Error Occured, Try again!") 


def view_expenses() -> None:
    try:
        with open("expenses.csv", "r") as f:
            print("Description  |  Amount")
            for i in csv.reader(f):
                print(f"{i[0]}  |  {i[1]}")
            print()
    except FileNotFoundError:
        print("File not found or No expenses found!")


def total_expenses() -> None:
    sum = 0
    try:
        with open("expenses.csv", "r") as f:
            for i in csv.reader(f):
                sum += float(i[1])

        print(f"Total Expenses: Rs {sum:.2f}\n")
    except FileNotFoundError:
        print("No expenses found!")


print("Welcome to Expense Tracker\n")

while True:
    print("Select an option from below:-")
    print("[1] Add Expense \n[2] View Expenses \n[3] Total Expenses \n")
    
    user = input("Type the option's number or type any character to EXIT: ")
    if user == "1":
        desc = input("Description: ")
        amount = float(input("Amount: "))
        add_expense(desc, amount)

    elif user == "2":
        view_expenses()

    elif user == "3":
        total_expenses()

    else:
        break