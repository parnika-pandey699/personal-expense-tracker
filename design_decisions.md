# Design Decisions

This section explains some of the main choices made while building the Personal Expense Tracker.

## 1. Python

Python was chosen because it is simple to work with and suitable for building a small command-line application.

It also allowed me to practice concepts such as classes, functions, modules, file handling, and error handling.

## 2. Command-Line Interface

The project uses a command-line interface instead of a graphical interface.

This keeps the project simple and allows the main focus to stay on the Python programming concepts used in the project.

## 3. CSV File for Storage

A CSV file was chosen to store expenses because the project only needs to manage simple expense records.

It is easy to read, write, and understand without setting up a separate database.

## 4. Separate Python Modules

The project is divided into different Python files based on their purpose.

For example, validation is handled in `validators.py`, storage is handled in `storage.py`, and reports are handled in `reports.py`.

This makes the code easier to understand and maintain.

## 5. Input Validation

Input validation was included so that common mistakes do not cause the program to stop unexpectedly.

For example, the program checks for empty text, invalid amounts, and invalid expense numbers.

## 6. Basic Testing

Separate test files were created to check important parts of the project.

The tests cover the `Expense` class, validation functions, expense management, and saving and loading data.