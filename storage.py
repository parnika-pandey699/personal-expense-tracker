import csv
import os

from expense import Expense


# Save expenses to CSV file
def save_expenses(
    expenses,
    filename="data/expenses.csv"
):

    with open(
        filename,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Date", "Category", "Description", "Amount"]
        )

        for expense in expenses:

            writer.writerow(
                [
                    expense.date,
                    expense.category,
                    expense.description,
                    expense.amount
                ]
            )


# Load expenses from CSV file
def load_expenses(
    filename="data/expenses.csv"
):

    expenses = []

    if not os.path.exists(filename):

        return expenses

    try:

        with open(filename, "r") as file:

            reader = csv.reader(file)

            # Skip the header row
            next(reader)

            for row in reader:

                if len(row) != 4:

                    print(
                        "Invalid row found in CSV. "
                        "Skipping it."
                    )

                    continue

                date = row[0]
                category = row[1]
                description = row[2]

                try:

                    amount = float(row[3])

                except ValueError:

                    print(
                        "Invalid amount found in CSV. "
                        "Skipping this expense."
                    )

                    continue

                expense = Expense(
                    date,
                    category,
                    description,
                    amount
                )

                expenses.append(expense)

    except OSError:

        print("Unable to read the expense file.")

    return expenses