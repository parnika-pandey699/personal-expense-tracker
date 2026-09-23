from expense import Expense
from reports import show_summary


class ExpenseManager:

    def __init__(self):
        self.expenses = []


    # Add a new expense
    def add_expense(
        self,
        date,
        category,
        description,
        amount
    ):

        expense = Expense(
            date,
            category,
            description,
            amount
        )

        self.expenses.append(expense)


    # View all expenses
    def view_expenses(self):

        if len(self.expenses) == 0:

            print("No expenses recorded.")
            return

        print("\n===== All Expenses =====")

        for expense in self.expenses:

            print("Date:", expense.date)
            print("Category:", expense.category)
            print("Description:", expense.description)
            print("Amount:", expense.amount)
            print("-------------------------")


    # Delete an expense
    def delete_expense(self, number):

        if number < 1 or number > len(self.expenses):

            return False

        del self.expenses[number - 1]

        return True


    # Search expenses
    def search_expenses(self, search_text):

        found = False

        print("\n===== Search Results =====")

        for expense in self.expenses:

            if (
                search_text.lower()
                in expense.category.lower()

                or

                search_text.lower()
                in expense.description.lower()
            ):

                print("Date:", expense.date)
                print("Category:", expense.category)
                print("Description:", expense.description)
                print("Amount:", expense.amount)
                print("-------------------------")

                found = True

        if not found:

            print("No matching expenses found.")


    # Show summary
    def show_summary(self):

        show_summary(self.expenses)