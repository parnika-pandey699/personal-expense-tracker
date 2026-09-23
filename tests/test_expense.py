import unittest

from expense import Expense


class TestExpense(unittest.TestCase):

    def test_expense_details(self):

        expense = Expense(
            "19/9/26",
            "Food",
            "Pizza",
            250
        )

        self.assertEqual(expense.date, "19/9/26")
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.description, "Pizza")
        self.assertEqual(expense.amount, 250)


if __name__ == "__main__":
    unittest.main()