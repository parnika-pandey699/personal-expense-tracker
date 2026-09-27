# Storage Design

The Personal Expense Tracker uses a CSV file to store expense information.

The file is named `expenses.csv` and is stored inside the `data` folder.

## Expense Data

Each expense contains the following information:

| Field | Description |
|---|---|
| Date | The date when the expense was made |
| Category | The category of the expense, such as food or travel |
| Description | A short description of the expense |
| Amount | The amount spent |

## CSV Structure

The CSV file uses the following columns:

```text
Date,Category,Description,Amount