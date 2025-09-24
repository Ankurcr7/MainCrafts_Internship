# Expense Tracker

import csv

def add_expense(desc: str, amount: float) -> None:
    try:
        f = open("expenses.csv", "a", newline="\n")
        writer = csv.writer(f)
        writer.writerow([desc, amount])
        f.close()

    except(Exception):
        print("Unexpected Error Occured, Try again!") 


def view_expenses() -> None:
    with open("expenses.csv", "r") as f:
        for i in csv.reader(f):
            print(f"Description: {i[0]}, Amount: {i[1]}")
        print()


def total_expenses() -> None:
    sum = 0
    with open("expenses.csv", "r") as f:
        for i in csv.reader(f):
            sum += float(i[1])

    print(f"Total Expenses: Rs {sum}\n")


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