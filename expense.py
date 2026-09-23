class Expense:

    def __init__(self, date, category, description, amount):

        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
expense = Expense(
    "20-09-2026",
    "Food",
    "Pizza",
    250
)

print(expense.date)
print(expense.category)
print(expense.description)
print(expense.amount)        