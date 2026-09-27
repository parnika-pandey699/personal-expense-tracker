# Process Workflow

The Personal Expense Tracker follows a simple menu-based workflow. The user selects an option, the program performs the requested task, and then returns to the main menu.

## Workflow Diagram

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
        |          Expenses           |
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

##  workflow steps                      
1. The program starts and loads previously saved expenses from the CSV file.
2. The main menu is displayed.
3. The user selects an option.
4. If the user adds an expense, the program takes the expense details, checks the input, and saves the expense.
5. If the user chooses to view or search expenses, the program displays the relevant records.
6. If the user chooses the summary option, the program calculates and displays the total and category-wise spending.
7. After completing an operation, the program returns to the main menu.
8. When the user selects Exit, the program ends.                   