# Personal Expense Tracker

## VITyarthi Build Your Own Project

### Final Project Report

**Project Title:** Personal Expense Tracker

**Technology Used:** Python

**Project Type:** Command-Line Application

**Student Name:** Parnika Pandey

**Institution:** VIT Bhopal University

**registration number:**26BCE10699

**Academic Year:** 2026

# 1. Introduction

The Personal Expense Tracker is a simple command-line application developed using Python.

The main purpose of this project is to help users record and manage their daily expenses in one place. The program allows the user to add expenses, view saved expenses, delete expenses, search for expenses, and view a summary of their spending.

The project was developed as a way to apply basic Python programming concepts in a practical project. It uses functions, classes, modules, file handling, input validation, error handling, and basic testing.

Expenses are stored in a CSV file so that the recorded information can be loaded again when the program is started.

The project follows a modular structure where different tasks are handled by separate Python files. This makes the program easier to understand, test, and maintain.

# 2. Problem Statement

Managing daily expenses can become difficult when expenses are not recorded properly or are written down in different places. It can also be difficult to know how much has been spent in total or which categories account for most of the spending.

The problem addressed by this project is the lack of a simple and organized way to record and manage personal expenses.

The Personal Expense Tracker provides a simple command-line solution where users can record their expenses, manage existing records, search for expenses, and view basic spending information.

# 3. Project Objectives

The main objectives of the Personal Expense Tracker are:

- To create a simple application for recording daily expenses.
- To allow users to view, search, and delete expense records.
- To calculate the total amount spent.
- To show spending category-wise.
- To store expense information so it can be used again later.
- To handle common invalid inputs without crashing the program.
- To practice Python concepts such as classes, functions, modules, file handling, validation, error handling, and testing.

# 4. Functional Requirements

The Personal Expense Tracker provides the following main functions:

## 4.1 Add Expense

The user can add a new expense by entering:

- Date
- Category
- Description
- Amount

The program validates the entered information before adding the expense.

## 4.2 View Expenses

The user can view all the expenses that have been recorded.

For each expense, the program displays its date, category, description, and amount.

## 4.3 Delete Expense

The user can select an expense from the list and delete it.

The program checks whether the selected expense number is valid before deleting it.

## 4.4 Search Expenses

The user can search for expenses using a category or description.

The program displays the expenses that match the entered search text.

## 4.5 View Expense Summary

The program calculates and displays:

- Number of expenses
- Total amount spent
- Category-wise spending

This provides a basic overview of the user's expenses.

## 4.6 Save and Load Expenses

The program stores expense records in a CSV file.

When the program starts, previously saved expenses are loaded automatically.

## 4.7 Handle Invalid Input

The program handles common input errors such as:

- Empty category or description
- Invalid amount
- Amount less than or equal to zero
- Invalid expense number
- Invalid menu choice

# 5. Non-Functional Requirements

The following requirements describe how the Personal Expense Tracker should behave.

## 5.1 Usability

The program should be simple and easy to use. The menu clearly displays the available options and provides understandable messages to the user.

## 5.2 Reliability

The program should correctly save and load expense records so that previously entered information is not lost when the program is closed.

## 5.3 Error Handling

The program should handle incorrect inputs without crashing. Invalid amounts, empty text, invalid expense numbers, and incorrect menu choices should be handled with suitable messages.

## 5.4 Maintainability

The project is divided into separate Python modules based on their purpose. This makes the code easier to understand, test, and modify.

## 5.5 Performance

The program should respond quickly for the normal amount of data expected in a personal expense tracker.

# 6. System Architecture

The Personal Expense Tracker follows a simple modular architecture. The user interacts with the program through the command-line menu, and different Python modules handle different responsibilities.

## 6.1 Architecture Diagram

```text
                    USER
                      |
                      v
                  main.py
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
     Expense      Validators   Reports
     Manager       Module       Module
          |
          v
       Storage
        Module
          |
          v
     expenses.csv


## 6.2 Main Components

### `main.py`

The main program displays the menu, takes input from the user, and connects the different modules.

### `expense.py`

This file contains the `Expense` class, which stores the details of an individual expense.

### `expense_manager.py`

This module manages the expense records. It handles adding, viewing, deleting, and searching expenses.

### `validators.py`

This module checks user input such as empty text, invalid amounts, and invalid expense numbers.

### `reports.py`

This module calculates the total spending and category-wise spending.

### `storage.py`

This module saves expenses to the CSV file and loads them when the program starts.

### `utils.py`

This module contains helper functions used by the project, such as formatting expense amounts.

### `data/expenses.csv`

This CSV file stores the expense records so that they can be loaded again when the application is started.  

# 7. Process Workflow

The Personal Expense Tracker follows a simple menu-based workflow. The user selects an option from the main menu, the program performs the requested operation, and then returns to the main menu.

## 7.1 Workflow Diagram

```text
                    START
                      |
                      v
               Load Expenses
                      |
                      v
                  Main Menu
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
   Add Expense    View/Search    View Summary
        |           Expenses          |
        v             |               |
      Save            |               |
        |             |               |
        +-------------+---------------+
                      |
                      v
                  Main Menu
                      |
                      v
                    Exit
                      |
                      v
                     END
```

## 7.2 Workflow Steps

1. The program starts and loads previously saved expenses from the CSV file.
2. The main menu is displayed.
3. The user selects an option.
4. If the user adds an expense, the program takes the expense details, validates the input, and saves the expense.
5. If the user chooses to view or search expenses, the program displays the relevant records.
6. If the user chooses the summary option, the program calculates and displays the total and category-wise spending.
7. After completing an operation, the program returns to the main menu.
8. When the user selects Exit, the program ends.

# 8. Storage Design

The Personal Expense Tracker uses a CSV file to store expense records. The file is named `expenses.csv` and is stored inside the `data` folder.

## 8.1 Expense Data

Each expense contains the following information:

| Field | Description |
|---|---|
| Date | The date when the expense was made |
| Category | The category of the expense, such as Food or Travel |
| Description | A short description of the expense |
| Amount | The amount spent |

## 8.2 CSV Structure

The CSV file contains the following columns:

```text
Date,Category,Description,Amount
```

Each row after the header represents one expense.

## 8.3 Data Handling

The `storage.py` module is responsible for saving and loading expense data.

When a new expense is added, the updated expense list is saved to the CSV file.

When the program starts, the saved expenses are loaded from the CSV file so that previously recorded data is available again.

# 9. Use Case Diagram

The use case diagram shows how the user interacts with the Personal Expense Tracker.

## 9.1 Use Case Diagram

```text
                 Personal Expense Tracker
              +--------------------------------+
              |                                |
              |       Add Expense              |
              |                                |
              |       View Expenses            |
              |                                |
      User -->|       Delete Expense           |
              |                                |
              |       Search Expenses           |
              |                                |
              |       View Expense Summary     |
              |                                |
              +--------------------------------+
```

## 9.2 Explanation

The user is the main actor in the Personal Expense Tracker.

The user can:

- Add a new expense.
- View recorded expenses.
- Delete an expense.
- Search for expenses by category or description.
- View a summary of spending.

The application is designed for a single user who manages their own personal expense records.

# 10. Class Diagram

The class diagram shows the main classes used in the Personal Expense Tracker and their relationship.

## 10.1 Class Diagram

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

## 10.2 Explanation

### Expense

The `Expense` class represents one expense record.

It stores:

- Date
- Category
- Description
- Amount

### ExpenseManager

The `ExpenseManager` class manages multiple expense records.

It stores `Expense` objects in a list and provides functions for adding, viewing, deleting, and searching expenses.

# 11. Sequence Diagram

The sequence diagram shows the interaction between the user and the different modules when a new expense is added.

## 11.1 Add Expense Sequence

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

## 11.2 Explanation

1. The user selects **Add Expense** from the main menu.
2. The user enters the expense details.
3. The program checks the input using the validation functions.
4. If the input is valid, the `ExpenseManager` creates an `Expense` object.
5. The expense is added to the expense list.
6. The updated expense list is saved to the CSV file.
7. The program displays a success message to the user.

# 12. Design Decisions

This section explains the main choices made while developing the Personal Expense Tracker.

## 12.1 Python

Python was chosen because it is simple to work with and suitable for building a small command-line application.

The project also provided an opportunity to practice classes, functions, modules, file handling, input validation, error handling, and testing.

## 12.2 Command-Line Interface

A command-line interface was used instead of a graphical interface.

This keeps the project simple and allows the main focus to remain on the Python programming concepts used in the project.

## 12.3 CSV File for Storage

A CSV file was chosen to store the expenses because the project only needs to manage simple expense records.

It is easy to read, write, and understand without setting up a separate database.

## 12.4 Separate Python Modules

The project is divided into different Python files based on their purpose.

For example, validation is handled in `validators.py`, storage is handled in `storage.py`, and reports are handled in `reports.py`.

This makes the code easier to understand and maintain.

## 12.5 Input Validation

Input validation was included so that common mistakes do not cause the program to stop unexpectedly.

For example, the program checks for empty text, invalid amounts, and invalid expense numbers.

## 12.6 Basic Testing

Separate test files were created to check important parts of the project.

The tests cover the `Expense` class, validation functions, expense management, and saving and loading data.

# 13. Implementation

The Personal Expense Tracker was implemented using Python and is divided into multiple modules. Each module has a specific responsibility.

## 13.1 Expense Management

The `Expense` class in `expense.py` stores the details of an individual expense.

The `ExpenseManager` class in `expense_manager.py` manages the collection of expenses and provides functions for:

- Adding expenses
- Viewing expenses
- Deleting expenses
- Searching expenses

## 13.2 Input Validation

The `validators.py` module contains functions used to validate user input.

The program checks:

- Whether text fields are empty
- Whether the expense amount is greater than zero
- Whether the selected expense number is valid

Invalid input is handled using suitable error messages instead of allowing the program to crash.

## 13.3 Data Storage

The `storage.py` module handles saving and loading expense records.

The expenses are stored in `data/expenses.csv` using Python's built-in `csv` module.

When an expense is added or deleted, the updated expense list is saved to the CSV file.

## 13.4 Expense Reports

The `reports.py` module generates a basic expense summary.

It calculates:

- Number of expenses
- Total amount spent
- Category-wise spending

The `utils.py` module is used to format the expense amounts for display.

## 13.5 Main Program

The `main.py` file provides the command-line menu and connects the different modules.

The main menu provides the following options:

1. Add Expense
2. View Expenses
3. Delete Expense
4. Search Expenses
5. View Summary
6. Exit

The program continues displaying the menu until the user selects the Exit option.

# 14. Screenshots and Results

The Personal Expense Tracker was tested by running the application through the command line and using its different menu options.

## 14.1 Main Menu

The main menu displays all the available options to the user.

**Screenshot: Main Menu**

_Insert the screenshot of the main menu here._

## 14.2 Adding an Expense

The user can enter the date, category, description, and amount to add a new expense.

**Screenshot: Adding an Expense**

_Insert the screenshot showing an expense being added successfully._

## 14.3 Viewing Expenses

The program displays the saved expenses along with their date, category, description, and amount.

**Screenshot: Viewing Expenses**

_Insert the screenshot showing the recorded expenses here._

## 14.4 Expense Summary

The summary displays the number of expenses, total amount spent, and category-wise spending.

**Screenshot: Expense Summary**

_Insert the screenshot of the expense summary here._

## 14.5 Test Results

The project was also tested using Python's built-in `unittest` module.

The tests were created for:

- Expense class
- Input validation
- Expense management
- Saving and loading expenses

All four individual test files completed successfully without errors.

**Screenshot: Test Results**

_Insert the screenshots showing the successful test results here._

# 15. Testing

Testing was performed to check whether the different parts of the Personal Expense Tracker work correctly.

## 15.1 Testing Method

Python's built-in `unittest` framework was used for automated testing.

The following test files were created:

| Test File | Purpose | Result |
|---|---|---|
| `test_expense.py` | Checks that expense details are stored correctly | Passed |
| `test_validators.py` | Checks input validation functions | Passed |
| `test_expense_manager.py` | Checks adding and deleting expenses | Passed |
| `test_storage.py` | Checks saving and loading expenses | Passed |

## 15.2 Test Commands

The following commands were used to run the tests:

```text
python3 -m unittest tests.test_expense
python3 -m unittest tests.test_validators
python3 -m unittest tests.test_expense_manager
python3 -m unittest tests.test_storage
```

All four test files completed successfully without errors.

## 15.3 Manual Testing

The application was also tested manually using the command-line menu.

The following features were checked:

- Adding an expense
- Viewing expenses
- Deleting an expense
- Searching for an expense
- Viewing the expense summary
- Saving and loading expenses
- Handling invalid input

The manual tests confirmed that the main features of the application were working as expected.

# 16. Challenges Faced

While developing the Personal Expense Tracker, I faced a few challenges during the implementation and testing of the project.

## 16.1 Handling Invalid User Input

One challenge was making sure that incorrect input did not cause the program to stop.

For example, entering text instead of a number for the expense amount caused a `ValueError`. This was handled using `try` and `except` so that the program could display an error message and continue running.

## 16.2 Organizing the Project into Modules

Another challenge was deciding how to divide the program into different Python files.

The project was separated into modules such as `expense.py`, `expense_manager.py`, `storage.py`, `validators.py`, and `reports.py`. This helped keep different parts of the program organized.

## 16.3 Saving and Loading Data

Handling the CSV file was another part that required attention.

The program needed to save the expenses correctly and load them again when it started. The `csv` module was used to handle this process.

## 16.4 Testing Individual Modules

Testing the different modules separately was also a learning experience.

Python's `unittest` module was used to test important parts of the project, including expense creation, validation, expense management, and storage.

# 17. Learnings

Developing the Personal Expense Tracker helped me understand how different Python concepts can be combined to create a complete project.

The main things I learned from this project are:

- How to create and use Python classes and objects.
- How to divide a program into separate modules.
- How to write and use functions.
- How to work with lists and dictionaries.
- How to read from and write to CSV files.
- How to validate user input.
- How to handle errors using `try` and `except`.
- How to write basic automated tests using Python's `unittest` module.
- How to organize a Python project into different files and folders.
- How to use Git for version control.
- How to use GitHub to store and share a project.

I also learned that testing and organizing code into separate modules makes it easier to find and fix problems in a project.

# 18. Future Enhancements

The current version of the Personal Expense Tracker focuses on basic expense management. The project can be improved further by adding more features in the future.

Some possible enhancements are:

- Add an option to edit an existing expense.
- Add date-based filtering of expenses.
- Add more detailed reports.
- Add charts to visualize spending.
- Add a graphical user interface (GUI).
- Use a database instead of a CSV file for storing larger amounts of data.
- Add user accounts and login functionality.
- Add monthly and yearly expense summaries.
- Add a budget feature to help users track spending limits.

# 19. References

The following resources were used while developing and documenting the project:

1. Python Documentation — Python programming language documentation.
2. Python `csv` Module Documentation — Used for reading and writing CSV files.
3. Python `unittest` Documentation — Used for automated testing.
4. Git Documentation — Used for version control.
5. GitHub Documentation — Used for hosting and sharing the project.
6. VITyarthi Build Your Own Project Guidelines — Used as the guideline for project development and documentation.