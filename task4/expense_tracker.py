import csv, os
from datetime import datetime

CSV_FILE= "expenses.csv"
HEADERS = ["id" , "date", "description", "amount", "category"]

def if_expense_file_exists():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="" ) as f:
            csv.writer(f).writerow(HEADERS)

def isEmpty(items: list) -> bool:
    if items:
         return False
    return True


def add_expense(desc: str, amount: str, category:str) -> None:
    try:
        amt = float(amount)
    except ValueError:
        print("Amount must be a number!")
        return

    row = [
            str(int(datetime.now().timestamp() * 1000)),
            datetime.now().strftime("%Y-%m-%d"),
            desc,
            f"{amt:.2f}",
            category
        ]
    with open(CSV_FILE, "a", newline='') as f:
        csv.writer(f).writerow(row)
        print("Successfully Added!")
                 

def view_expenses() -> None:
    if_expense_file_exists()
    with open(CSV_FILE, "r") as f:
            rows = list(csv.reader(f))
    if len(rows) <= 1:
            print("No Expense Found!!")
            return
    total = 0
    for i in rows[1:]:
            print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}")
            total += float(i[3])
    
    print(f"\nTotal expense: {total}")


def search_category(category:str) -> None:
    if_expense_file_exists()
    with open(CSV_FILE, "r" ) as f:
            rows = list(csv.reader(f))[1:]
    
    total = 0
    result = [i for i in rows if i[4].lower().strip() == category.lower().strip()]
    if isEmpty(result):
            print(f"No expenses found for '{category.strip()}' category!")
    else:
        for i in result:
            print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}")
            total += float(i[3])
    
        print(f"\nTotal expense for {category} category: {total}")


def delete_by_id(id:str) -> None:
    if_expense_file_exists()
    with open(CSV_FILE, "r") as f:
        rows = list(csv.reader(f))[1:]
        updated_row = [row for row in rows if row[0] != id]
        
    with open(CSV_FILE, "w", newline='') as f:
        csv.writer(f).writerow(HEADERS)
        csv.writer(f).writerows(updated_row)
             
             

def total_monthly_spent(month: str) -> None:
    if_expense_file_exists()
    with open(CSV_FILE, "r") as f:
        rows = list(csv.reader(f))[1:]

    result = [i for i in rows if i[1].strip().startswith(month)]
    if isEmpty(result):
        print(f"No expenses found for '{month}' month!")
    else:
        total = sum(float(i[3]) for i in result)
        print(f"Monthly total for {month}: {total:.2f}")


def run():
    if_expense_file_exists()
    while True:
        print("\nSelect an option from below:-")
        print("[1] Add Expense \n[2] View Expenses \n[3] Search Category \n[4] Total monthly spent \n[5] Delete by ID \n[6 or any character] Exit \n")
        
        user = input("Type the option's number or type any character to EXIT: ")
        if user == "1": #
            desc = input("Description: ").strip()
            amount = input("Amount: ").strip()
            category = input("Category: ").strip()
            add_expense(desc, amount, category)

        elif user == "2": #
            view_expenses()

        elif user == "3": #
            search_category(input("Enter a Category: ").strip())

        elif user == "4": 
            total_monthly_spent(input("Enter month(YYYY-MM): ").strip())

        elif user == "5": #
            delete_by_id(input("Enter a ID: ").strip())

        else:
            break


if __name__ == "__main__":
    print("Welcome to Expense Tracker")   
    run()