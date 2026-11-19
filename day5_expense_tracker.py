import json
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load_expenses() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: expenses.json is corrupted, starting with an empty list.")
        return []


def save_expenses(expenses: list[dict]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses: list[dict]) -> None:
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount, expense not added.")
        return
    if amount <= 0:
        print("Amount must be positive, expense not added.")
        return
    category = input("Category: ").strip()
    note = input("Note: ").strip()
    if not category:
        print("Category cannot be empty, expense not added.")
        return
    expenses.append({"amount": amount, "category": category, "note": note})
    save_expenses(expenses)
    print(f"Added: {category} - ${amount:.2f} - {note}")


def list_expenses(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['category']} - ${e['amount']:.2f} - {e['note']}")


def show_totals(expenses: list[dict]) -> None:
    totals: dict[str, float] = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    for category in sorted(totals):
        print(f"{category}: ${totals[category]:.2f}")
    print(f"Total: ${sum(totals.values()):.2f}")


def max_profit(prices: list[int]) -> int:
    min_price = prices[0]
    best = 0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > best:
            best = profit
    return best


def main() -> None:
    print(f"DSA: [7, 1, 5, 3, 6, 4] -> {max_profit([7, 1, 5, 3, 6, 4])}")
    print(f"DSA: [7, 6, 4, 3, 1] -> {max_profit([7, 6, 4, 3, 1])}")
    expenses = load_expenses()
    while True:
        print("\n1. Add expense")
        print("2. List expenses")
        print("3. Show totals")
        print("4. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            show_totals(expenses)
        elif choice == "4":
            print("Saved to expenses.json. Bye!")
            break
        else:
            print("Invalid choice, pick 1-4.")


if __name__ == "__main__":
    main()