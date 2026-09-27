# Testing

The project was tested using Python's built-in `unittest` module.

## Automated Tests

The following parts of the project were tested:

| Test File | What It Checks | Result |
|---|---|---|
| `test_expense.py` | Checks that expense details are stored correctly | Passed |
| `test_validators.py` | Checks input validation functions | Passed |
| `test_expense_manager.py` | Checks adding and deleting expenses | Passed |
| `test_storage.py` | Checks saving and loading expenses | Passed |

## Test Commands

The tests were run using the following commands:

```text
python3 -m unittest tests.test_expense
python3 -m unittest tests.test_validators
python3 -m unittest tests.test_expense_manager
python3 -m unittest tests.test_storage
```

All four test files completed successfully without errors.

## Manual Testing

The program was also tested manually by using the menu options.

The following features were checked:

- Adding an expense
- Viewing expenses
- Deleting an expense
- Searching for an expense
- Viewing the expense summary
- Saving and loading expenses
- Handling invalid input