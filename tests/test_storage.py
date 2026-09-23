import unittest
import os

from expense import Expense
from storage import save_expenses, load_expenses


class TestStorage(unittest.TestCase):

    def test_save_and_load(self):

        test_file = "data/test_expenses.csv"

        expenses = [
            Expense(
                "19/9/26",
                "Food",
                "Pizza",
                250
            ),
            Expense(
                "19/9/26",
                "Travel",
                "Bus",
                50
            )
        ]

        save_expenses(
            expenses,
            test_file
        )

        loaded_expenses = load_expenses(
            test_file
        )

        self.assertEqual(
            len(loaded_expenses),
            2
        )

        self.assertEqual(
            loaded_expenses[0].description,
            "Pizza"
        )

        self.assertEqual(
            loaded_expenses[0].amount,
            250
        )

        self.assertEqual(
            loaded_expenses[1].description,
            "Bus"
        )

        self.assertEqual(
            loaded_expenses[1].amount,
            50
        )

        # Remove the test file
        if os.path.exists(test_file):
            os.remove(test_file)


if __name__ == "__main__":
    unittest.main()