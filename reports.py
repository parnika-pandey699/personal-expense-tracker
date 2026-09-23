from utils import format_amount


def show_summary(expenses):

    if len(expenses) == 0:

        print("No expenses recorded.")
        return

    total = 0

    category_totals = {}

    for expense in expenses:

        total = total + expense.amount

        category = expense.category

        if category in category_totals:

            category_totals[category] = (
                category_totals[category]
                + expense.amount
            )

        else:

            category_totals[category] = expense.amount

    print("\n===== Expense Summary =====")

    print(
        "Number of Expenses:",
        len(expenses)
    )

    print(
        "Total Expenses:",
        format_amount(total)
    )

    print(
        "\n===== Category-wise Spending ====="
    )

    for category in category_totals:

        print(
            category + ":",
            format_amount(category_totals[category])
        )