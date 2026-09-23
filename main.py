from storage import save_expenses, load_expenses
from expense_manager import ExpenseManager
from validators import (
    is_valid_text,
    is_valid_amount,
    is_valid_expense_number
)


print("=================================")
print("   PERSONAL EXPENSE TRACKER")
print("=================================")


# Create ExpenseManager
manager = ExpenseManager()


# Load saved expenses
manager.expenses = load_expenses()


choice = ""


while choice != "6":

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Search Expenses")
    print("5. View Summary")
    print("6. Exit")

    choice = input("\nEnter your choice: ")


    # Add Expense
    if choice == "1":

        date = input("Enter date: ")

        description = input(
            "Enter expense description: "
        )

        if not is_valid_text(description):

            print("\nDescription cannot be empty.")

            continue

        try:

            amount = float(
                input("Enter expense amount: ")
            )

            if not is_valid_amount(amount):

                print(
                    "\nAmount must be greater than zero."
                )

                continue

        except ValueError:

            print(
                "\nInvalid amount. "
                "Please enter a number."
            )

            continue

        category = input(
            "Enter expense category: "
        )

        if not is_valid_text(category):

            print("\nCategory cannot be empty.")

            continue

        # Add expense through ExpenseManager
        manager.add_expense(
            date,
            category,
            description,
            amount
        )

        # Save updated expenses
        save_expenses(manager.expenses)

        print("\nExpense added successfully!")


    # View Expenses
    elif choice == "2":

        manager.view_expenses()


    # Delete Expense
    elif choice == "3":

        if len(manager.expenses) == 0:

            print("\nNo expenses to delete.")

        else:

            print("\n===== Expenses =====")

            for i in range(len(manager.expenses)):

                print(
                    i + 1,
                    ".",
                    manager.expenses[i].description,
                    "-",
                    manager.expenses[i].amount
                )

            try:

                delete_number = int(
                    input(
                        "\nEnter expense number to delete: "
                    )
                )

            except ValueError:

                print(
                    "\nPlease enter a valid "
                    "expense number."
                )

                continue

            if not is_valid_expense_number(
                delete_number,
                len(manager.expenses)
            ):

                print("\nInvalid expense number!")

                continue

            manager.delete_expense(delete_number)

            # Save updated expenses
            save_expenses(manager.expenses)

            print(
                "\nExpense deleted successfully!"
            )


    # Search Expenses
    elif choice == "4":

        if len(manager.expenses) == 0:

            print("\nNo expenses recorded.")

        else:

            search_text = input(
                "\nEnter category or description "
                "to search: "
            )

            if not is_valid_text(search_text):

                print("\nSearch text cannot be empty.")

                continue

            manager.search_expenses(search_text)


    # View Summary
    elif choice == "5":

        manager.show_summary()


    # Exit
    elif choice == "6":

        print(
            "\nExiting Personal Expense Tracker..."
        )


    # Invalid Menu Choice
    else:

        print("\nInvalid choice!")


print(
    "Thank you for using Personal Expense Tracker!"
)
