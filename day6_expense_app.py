from expenses_store import load_expenses, save_expenses
from expenses_report import format_expenses, format_totals

SAMPLE_EXPENSES = [
    {"amount": 12.00, "category": "Food", "note": "Lunch"},
    {"amount": 38.50, "category": "Food", "note": "Groceries"},
    {"amount": 25.00, "category": "Transport", "note": "Bus pass"},
]

def main():
    save_expenses(SAMPLE_EXPENSES)
    expenses = load_expenses()
    print("Expenses:")
    print(format_expenses(expenses))
    print()
    print("Totals per category:")
    print(format_totals(expenses))

if __name__ == "__main__":
    main()