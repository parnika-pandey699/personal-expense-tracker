# Class Diagram

## Purpose

The class diagram shows the main classes used in the Personal Expense Tracker and how they are related.

## Diagram

```text
+---------------------------+
|          Expense          |
+---------------------------+
| - date                    |
| - category                |
| - description             |
| - amount                  |
+---------------------------+

              ^
              |
              | creates and stores
              |
+---------------------------+
|      ExpenseManager       |
+---------------------------+
| - expenses                |
+---------------------------+
| + add_expense()           |
| + view_expenses()         |
| + delete_expense()        |
| + search_expenses()       |
| + show_summary()          |
+---------------------------+
```

## Explanation

### Expense

The `Expense` class stores the details of one expense:

- Date
- Category
- Description
- Amount

### ExpenseManager

The `ExpenseManager` class keeps track of the expenses and provides functions to add, view, delete, and search expenses.

It stores multiple `Expense` objects in a list.