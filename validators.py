def is_valid_text(text):
    return text.strip() != ""


def is_valid_amount(amount):
    return amount > 0


def is_valid_expense_number(number, total_expenses):
    return 1 <= number <= total_expenses