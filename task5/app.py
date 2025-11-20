import argparse
import sqlite3
import logging
import sys
from datetime import datetime
from typing import Optional, List


DB_FILE = "expenses.db"
LOG_FILE = "app.log"
TABLE_SCHEMA = """
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    description TEXT,
    amount REAL NOT NULL,
    category TEXT
)
"""


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def db_connect(db_file: str = DB_FILE) -> sqlite3.Connection:
    try:
        conn = sqlite3.connect(db_file, detect_types=sqlite3.PARSE_DECLTYPES)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute(TABLE_SCHEMA)
        conn.commit()
        return conn

    except Exception as e:
        logging.error("Failed to connect to DB", exc_info=True)
        print("Failed to connect to DB. See 'app.log' for more details!")
        sys.exit(1)


def validate_amount(amount: str) -> float:
    try:
        amt = float(amount)
    except ValueError:
        print("Amount must be a number (e.g., 12.50).")
    if not (amt > 0):
        print("Amount must be greater than 0.")

    return amt


def titleCase(cat: Optional[str]) -> Optional[str]:
    if cat is None:
        return None
    return cat.strip().title()



def add_expense(description:str, amount:float, category: Optional[str], date_str:Optional[str] ) -> Optional[str]:
    try:
        if date_str:
            try:
                parsed = datetime.strptime(date_str, "%Y-%m-%d")
                date_val  = parsed.strftime("%Y-%m-%d")
            except ValueError :
                print("Date must be in YYYY-MM-DD format.")

        else:
            date_val = datetime.now().strftime("%Y-%m-%d")

        conn = db_connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO expenses (date, description, amount, category) VALUES (?, ?, ?, ?)",
            (date_val, description, amount, category),
        )
        conn.commit()
        new_id = cur.lastrowid
        conn.close()

        msg = f"Added expense id={new_id} - {date_val} {description} {amount:.2f} {category or ''}".strip()
        print(msg)
        logging.info("add: %s", msg)


    except Exception as e:
        logging.error("Error adding expense", exc_info=True)
        print("Error: could not add expense -", str(e))


def list_expenses(month: Optional[str] = None):
    try:
        conn = db_connect()
        cur = conn.cursor()

        if month:
            try:
                datetime.strptime(month + "-01", "%Y-%m-%d")
            except ValueError:
                print("Month must be in YYYY-MM format.")

            like_pattern = month + "-%"
            cur.execute("""
                select id, date, description, amount, category from expenses where date like ? order by date""", (like_pattern,))
        else:
            cur.execute("""
                select id, date, description, amount, category from expenses order by id""")
            
        
        rows = cur.fetchall()
        conn.close()

        if not rows:
            print("No expenses found!")
            return
        
        print(f"{'ID':>3}  {'Date':10}  {'Amount':>10}  {'Category':12}  Description")
        print("-" * 70)
        for r in rows:
            id_, date_, desc, amt, cat = r
            desc_display = (desc or "")[:40]
            print(f"{id_:>3}  {date_:10}  {amt:10.2f}  { (cat or ''):12}  {desc_display}")
        logging.info("list: month=%s count=%d", month, len(rows))


    except Exception as e:
        logging.error("Error listing expenses", exc_info=True)
        print("Error: could not list expenses -", str(e))



def report(by):
    try: 
        conn = db_connect()
        cur = conn.cursor()

        if by == "month":
            query = """
                SELECT SUBSTR(date,1,7) AS month, SUM(amount) AS total, COUNT(*) AS cnt
                FROM expenses
                GROUP BY month
                ORDER BY month DESC
            """
        elif by == "category":
            query = """
                SELECT category, SUM(amount) AS total, COUNT(*) AS cnt
                FROM expenses
                GROUP BY category
                ORDER BY total DESC
            """

        rows = cur.execute(query).fetchall()
        conn.close()

        if not rows:
            print("No data to report")
            return
        
        for key, total, cnt in rows:
            print(f"{key:<12} -> Rs{total:.2f} ({cnt} items)")

        logging.info(f"report: by={by} rows=%d", len(rows))

    except Exception as e:
        logging.error(f"Error generating {by} report", exc_info=True)
        print(f"Error: could not generate {by} report -", str(e))



def delete_expense(expense_id: int):
    try:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute("SELECT id, date, description, amount, category FROM expenses WHERE id = ?", (expense_id,))
        row = cur.fetchone()

        if not row:
            print(f"No expense found with id={expense_id}.")
            return
        cur.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        conn.close()
        msg = f"Deleted expense id={expense_id}"
        print(msg)
        logging.info("delete: id=%d", expense_id)


    except Exception as e:
        logging.error("Error deleting expense", exc_info=True)
        print("Error: could not delete expense -", str(e))


def parse_args(argv: Optional[List[str]] = None):
    parser = argparse.ArgumentParser(prog="ExpenseTracker", description="Simple CLI expense tracker (SQLite).")
    sub = parser.add_subparsers(dest="command", required=True)

    # add
    p_add = sub.add_parser("add", help="Add an expense")
    p_add.add_argument("--desc", required=True, help="Description")
    p_add.add_argument("--amount", required=True, help="Amount (numeric, >0)")
    p_add.add_argument("--category", required=False, help="Category (optional)")
    p_add.add_argument("--date", required=False, help="Date YYYY-MM-DD (optional, defaults to today)")

    # list
    p_list = sub.add_parser("list", help="List expenses")
    p_list.add_argument("--month", required=False, help="Filter by month YYYY-MM")

    # report
    p_report = sub.add_parser("report", help="Generate report")
    p_report.add_argument("--by", choices=["category", "month"], default="category", help="Group report by category or month")

    # delete
    p_delete = sub.add_parser("delete", help="Delete an expense by id")
    p_delete.add_argument("--id", required=True, type=int, help="ID of the expense to delete")

    return parser.parse_args(argv)


def app(argv: Optional[List[str]] = None):
    args = parse_args(argv)
    try:
        if args.command == "add":
            try:
                amt = validate_amount(args.amount)
            except ValueError as ve:
                print("Validation error:", ve)
                return
            cat = titleCase(args.category)
            add_expense(args.desc.strip(), amt, cat, args.date)

        elif args.command == "list":
            list_expenses(month=args.month)

        elif args.command == "report":
            report(args.by)

        elif args.command == "delete":
            delete_expense(args.id)

        else:
            print("Unknown command. Use -h for help.")

    except Exception as e:
        logging.error("Unexpected error in app", exc_info=True)
        print("An unexpected error occurred. See app.log for details!")



if __name__ == "__main__":
    app()