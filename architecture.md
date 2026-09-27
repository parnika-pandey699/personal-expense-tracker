# System Architecture

The Personal Expense Tracker is a command-line application written in Python.

The user interacts with the program through the main menu. The main program then uses different modules to handle expenses, validate input, generate reports, and store data.

```text
## Architecture Diagram


                 USER
                   |
                   v
                main.py
                   |
        +----------+----------+
        |          |          |
        v          v          v
   Expense      Validators  Reports
   Manager       Module      Module
        |
        v
     Storage
      Module
        |
        v
    expenses.csv


    ## Main Components

### main.py

This is the main part of the program. It displays the menu and takes input from the user.

### expense.py

This file contains the `Expense` class, which stores the details of an expense.

### expense_manager.py

This module manages the expenses. It handles adding, viewing, deleting, and searching expenses.

### validators.py

This module checks user input, such as empty text, invalid amounts, and invalid expense numbers.

### reports.py

This module calculates the total spending and category-wise spending.

### storage.py

This module saves expenses to the CSV file and loads them when the program starts.

### utils.py

This module contains small helper functions, such as formatting the expense amount.

### expenses.csv

This is the CSV file where the expense records are stored.