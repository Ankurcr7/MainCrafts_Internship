# ExpenseTracker (SQLite CLI)

A simple command-line expense tracker that stores expenses in `expenses.db` (SQLite),
provides non-interactive CLI commands using `argparse`, and logs actions to `app.log`.

## Requirements
- Python 3.8+
- No external packages (uses stdlib sqlite3, argparse, logging)

## Files
- `app.py` — main CLI application
- `expenses.db` — SQLite database (auto-created)
- `app.log` — action and error log (created automatically)

## Install / Run
1. Save `app.py` to a folder.
2. Run commands with Python:

### Examples

Add an expense:

```
python app.py add --desc "Coffee" --amount 60 --category Food
```

List all expenses:

```
python app.py list
```

List expenses for October 2025:

```
python app.py list --month 2025-10
```

Report totals by category:

```
python app.py report --by category
```

Report totals by month:

```
python app.py report --by month
```

Delete an expense:

```
python app.py delete --id 17
```
