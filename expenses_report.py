def totals_per_category(expenses):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]
    return totals

def format_expenses(expenses):
    if not expenses:
        return "No expenses yet."
    lines = [f'{e["note"]} ({e["category"]}): ${e["amount"]:.2f}' for e in expenses]
    return "\n".join(lines)

def format_totals(expenses):
    totals = totals_per_category(expenses)
    lines = [f"{category}: ${total:.2f}" for category, total in totals.items()]
    lines.append(f"Grand total: ${sum(totals.values()):.2f}")
    print(f"Item: {len(expenses)}")
    return "\n".join(lines)