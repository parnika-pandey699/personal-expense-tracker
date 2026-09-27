# Functional Requirements

The Personal Expense Tracker is a command-line Python program that helps a user record and manage their daily expenses.

## 1. Add Expense

The user should be able to add a new expense by entering:

- Date
- Category
- Description
- Amount

The program checks that the description and category are not empty and that the amount is greater than zero.

After the expense is added, it is saved in the CSV file.

## 2. View Expenses

The user should be able to view all the expenses that have been recorded.

For each expense, the program displays:

- Date
- Category
- Description
- Amount

If there are no expenses, the program should show a suitable message instead.

## 3. Delete Expense

The user should be able to delete an expense by selecting its number from the list.

The program should check that the selected number is valid before deleting the expense.

After deletion, the updated expense list is saved to the CSV file.

## 4. Search Expenses

The user should be able to search for an expense using its category or description.

The program displays the expenses that match the search text.

If no matching expense is found, the program informs the user.

## 5. View Expense Summary

The program should calculate and display:

- Number of recorded expenses
- Total amount spent
- Amount spent in each category

This gives the user a quick view of their spending.

## 6. Save and Load Expenses

The program should save expenses in a CSV file so that the data is not lost when the program is closed.

When the program starts again, previously saved expenses should be loaded automatically.

## 7. Handle Invalid Input

The program should handle common input mistakes without crashing.

For example:

- Empty category or description
- Invalid amount
- Amount less than or equal to zero
- Invalid expense number
- Invalid menu choice