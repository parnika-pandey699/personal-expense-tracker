# Sequence Diagram

## Purpose

The sequence diagram shows the steps involved when a user adds a new expense to the Personal Expense Tracker.

## Add Expense Flow

```text
User          main.py       Validators     ExpenseManager      Storage
 |               |              |                |               |
 |-- Add Expense->|              |                |               |
 |               |              |                |               |
 |-- Enter details>|             |                |               |
 |               |              |                |               |
 |               |-- Check input->|              |               |
 |               |<-- Valid input-|              |               |
 |               |                                |               |
 |               |-- Add expense----------------->|               |
 |               |                                |               |
 |               |                                |-- Create Expense
 |               |                                |               |
 |               |                                |-- Save expense->|
 |               |                                |               |
 |               |                                |<-- Saved -------|
 |               |<-- Success message-------------|               |
 |<-- Expense added|                             |               |
```

## Explanation

1. The user selects **Add Expense** from the main menu.
2. The user enters the date, description, amount, and category.
3. The program checks the input using the validation functions.
4. If the input is valid, `ExpenseManager` creates an `Expense` object.
5. The expense is added to the expense list.
6. The `storage.py` module saves the updated expenses to the CSV file.
7. The program shows a success message to the user.