#Personal Expense Tracker
## About the Project

This is a simple personal expense tracker made by using python

I made this project to keep track of everyday expenses.The program runs in the terminal and allows the user to add expenses,view them,delete them,search for specific expenses,and see a summary of spending

## Features
The currently allows the user to:
- add a new expense
- view all saved expenses
- delete an expense
- search expense ny category or discription
- save the total amount spent
- save expenses in a CSV file
- load saved expenses when the program starts 
- handle invalid inputs such as empty texts and invalid amount

## Technologies used
-Python
-CSV file 
-Git
-GitHub

## Project structure
personal-expense-tracker/
│
├── main.py
├── expense.py
├── expense_manager.py
├── storage.py
├── reports.py
├── validators.py
├── utils.py
│
├── data/
│   └── expenses.csv
│
├── tests/
│   ├── __init__.py
│   ├── test_expense.py
│   ├── test_validators.py
│   ├── test_expense_manager.py
│   └── test_storage.py
│
├── README.md
├── statement.md
└── .gitignore

## How to run
open the project folder in the terminal and run:
python3 main.py

## Example menu
- Add Expense
- View Expenses
- Delete Expense
- Search Expenses
- View Summary
- Exit

## Testing 
the tests can be run using:
python3 -m unittest tests.test_expense
python3 -m unittest tests.test_validators
python3 -m unittest tests.test_expense_manager
python3 -m unittest tests.test_storage

## What I learned
- Working with python classes and objects
- using functions and separate python modules
- reading and writing CSV files
- Handling user input
- Handling errors using try and except
- Organizing a python project into different files
- writing basic unit tests
- using Git and GitHub to manage project

 ## Future improvements
- Editing an existing expense
- Adding more detailed reports
- Filtering expenses by date
- Adding a graphical interface
- Adding charts for spending



