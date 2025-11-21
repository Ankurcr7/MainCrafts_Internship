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



## Behavior & Validation
- Amount must be numeric and > 0.
- Category is normalized to Title Case.
- Date must be `YYYY-MM-DD` when provided; otherwise today's date is used.
- Helpful error messages are printed; emergencies/errors are logged to `app.log`.

## Logging
- All user actions (add/list/report/delete) are logged at INFO level to `app.log`.
- Unexpected exceptions are logged at ERROR level with stack traces.

## Example outputs
(See `examples` section in this README for sample terminal captures.)

## Screenshot
If you captured terminal output or screenshots, place them in the repo. Example uploaded screenshot path:
`/mnt/data/47d384c0-fe2d-45b0-9aae-f8535a2933c1.png`
