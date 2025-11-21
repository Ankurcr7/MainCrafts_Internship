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


Add two expenses:

```python

$ python app.py add --desc "Coffee" --amount 60 --category Food
Added expense id=1 - 2025-11-19 Coffee 60.00 Food

$ python app.py add --desc "Electricity bill" --amount 1250.5 --category utilities --date 2025-11-01
Added expense id=2 - 2025-11-01 Electricity bill 1250.50 Utilities

```

List all:

```python 

$ python app.py list
 ID  Date        Amount      Category      Description
----------------------------------------------------------------------
  1  2025-11-19      60.00  Food          Coffee
  2  2025-11-01    1250.50  Utilities     Electricity bill
```


List by month:

```python

$ python app.py list --month 2025-11
 ID  Date        Amount      Category      Description
----------------------------------------------------------------------
  1  2025-11-19      60.00  Food          Coffee
  2  2025-11-01    1250.50  Utilities     Electricity bill

```

Report by category:

```python 

$ python app.py report --by category
Shopping     -> Rs4339.00 (4 items)
Health       -> Rs2340.00 (3 items)
```


Report by month:

```python
$ python app.py report --by month
2025-11      -> Rs7224.50 (17 items)
2025-10      -> Rs820.00 (1 items)

```


Delete:

```python

$ python app.py delete --id 1
Deleted expense id=1

```


If an error occurs (invalid amount):

```python
$ python app.py add --desc "Bad" --amount abc --category Food
Validation error: Amount must be a number (e.g., 12.50).

```