# Expense Tracker 2.0

import csv
import datetime


def add_expense(desc: str, amount: float, category:str) -> None:
    try:
        f = open("expenses.csv", "a", newline="\n")
        writer = csv.writer(f)
        writer.writerow([desc, amount, category, datetime.datetime.now().strftime("%Y-%m-%d")])

        print("Successfully Added!\n")

    except Exception:
        print("Unexpected Error Occured, Try again!") 


def view_expenses() -> None:
    try:
        with open("expenses.csv", "r") as f:
            print("Description  |  Amount  |  Category  |  Date")
            for i in csv.reader(f):
                print(f"{i[0]}  |  {i[1]}  |  {i[2]}  |  {i[3]}")
            print()
    except FileNotFoundError:
        print("File not found or No expenses found!")


def search_category(category:str) -> None:
    try:
        with open("expenses.csv", "r") as f:
            for i in csv.reader(f):
                if i[2].lower() == category.lower():
                    print(i)

            print()

    except FileNotFoundError:
        print("File not found or No expenses found!")


def total_spent_by_category(category:str) -> None:
    try:
        with open("expenses.csv", "r") as f:
            sum = 0
            for i in csv.reader(f):
                if i[2].lower() == category.lower():
                    sum += float(i[1])
            print(f"Total spent in {category}: {sum:.2f}\n")
    except FileNotFoundError:
        print("No expenses found!")
                

def total_monthly_spent(month: str) -> None:
    try:
        with open("expenses.csv", "r") as f:
            sum = 0
            for i in csv.reader(f):
                if i[3].startswith(month):
                    sum += float(i[1])
            print(f"Monthly total: {sum:.2f}\n")
    except FileNotFoundError:
        print("No expenses found!")


def total_expenses() -> None:
    sum = 0
    try:
        with open("expenses.csv", "r") as f:
            for i in csv.reader(f):
                sum += float(i[1])

        print(f"Total Expenses: {sum:.2f}\n")
    except FileNotFoundError:
        print("No expenses found!")



print("Welcome to Expense Tracker\n")

while True:
    print("Select an option from below:-")
    print("[1] Add Expense \n[2] View Expenses \n[3] Search Category \n[4] Total spent per Category \n[5] Total monthly spent \n[6] Total Expenses \n")
    
    user = input("Type the option's number or type any character to EXIT: ")
    if user == "1":
        desc = input("Description: ")
        amount = float(input("Amount: "))
        category = input("Category: ")
        add_expense(desc, amount, category)

    elif user == "2":
        view_expenses()

    elif user == "3":
        category = input("Enter a Category: ")
        search_category(category)

    elif user == "4":
        category = input("Enter a Category: ")
        total_spent_by_category(category)

    elif user == "5":
        month = input("Enter month(YYYY-MM): ")
        total_monthly_spent(month)

    elif user == "6":
        total_expenses()

    else:
        break