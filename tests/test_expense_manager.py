import unittest

from expense_manager import ExpenseManager


class TestExpenseManager(unittest.TestCase):

    def test_add_expense(self):

        manager = ExpenseManager()

        manager.add_expense(
            "19/9/26",
            "Food",
            "Pizza",
            250
        )

        self.assertEqual(
            len(manager.expenses),
            1
        )

        self.assertEqual(
            manager.expenses[0].description,
            "Pizza"
        )

        self.assertEqual(
            manager.expenses[0].amount,
            250
        )


    def test_delete_expense(self):

        manager = ExpenseManager()

        manager.add_expense(
            "19/9/26",
            "Food",
            "Pizza",
            250
        )

        result = manager.delete_expense(1)

        self.assertTrue(result)

        self.assertEqual(
            len(manager.expenses),
            0
        )


    def test_invalid_delete(self):

        manager = ExpenseManager()

        result = manager.delete_expense(1)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()