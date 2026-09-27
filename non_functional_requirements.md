# Non-Functional Requirements

These requirements describe how the Personal Expense Tracker should behave while the user is using it.

## 1. Usability

The program should be easy to use for someone who is not familiar with complicated software.

The menu should clearly show the available options, and the program should give simple messages when the user enters information.

## 2. Reliability

The program should save expenses correctly and load them again when it is started.

It should also avoid losing existing expenses when a new expense is added or deleted.

## 3. Error Handling

The program should handle incorrect input without suddenly stopping.

For example, if the user enters an invalid amount or selects an incorrect expense number, the program should show an error message and allow the user to continue.

## 4. Maintainability

The code should be divided into separate Python files based on their purpose.

For example, expense management, data storage, validation, and reports are kept in separate modules.

This makes the project easier to understand and update.

## 5. Performance

The program should respond quickly when adding, viewing, searching, or deleting expenses.

Since this project is designed for normal personal use, it should work smoothly with a reasonable number of expense records.