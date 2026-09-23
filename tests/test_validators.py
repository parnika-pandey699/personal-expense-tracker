import unittest

from validators import (
    is_valid_text,
    is_valid_amount,
    is_valid_expense_number
)


class TestValidators(unittest.TestCase):

    def test_valid_text(self):

        self.assertTrue(
            is_valid_text("Food")
        )

    def test_empty_text(self):

        self.assertFalse(
            is_valid_text("")
        )

    def test_valid_amount(self):

        self.assertTrue(
            is_valid_amount(250)
        )

    def test_invalid_amount(self):

        self.assertFalse(
            is_valid_amount(0)
        )

        self.assertFalse(
            is_valid_amount(-50)
        )

    def test_valid_expense_number(self):

        self.assertTrue(
            is_valid_expense_number(2, 5)
        )

    def test_invalid_expense_number(self):

        self.assertFalse(
            is_valid_expense_number(0, 5)
        )

        self.assertFalse(
            is_valid_expense_number(6, 5)
        )


if __name__ == "__main__":
    unittest.main()