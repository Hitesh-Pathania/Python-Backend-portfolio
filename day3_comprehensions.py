orders = [
    {"id": 1, "customer": "Aisha", "amount": 120},
    {"id": 2, "customer": "Ben", "amount": 75},
    {"id": 3, "customer": "Carlos", "amount": 200},
    {"id": 4, "customer": "Aisha", "amount": 80},
    {"id": 5, "customer": "Dana", "amount": 150},
    {"id": 6, "customer": "Ben", "amount": 125},
    {"id": 7, "customer": "Eli", "amount": 60},
    {"id": 8, "customer": "Carlos", "amount": 50},
    {"id": 9, "customer": "Aisha", "amount": 100},
    {"id": 10, "customer": "Dana", "amount": 90},
    {"id": 11, "customer": "Eli", "amount": 140},
    {"id": 12, "customer": "Ben", "amount": 50},
    {"id": 13, "customer": "Carlos", "amount": 175},
    {"id": 14, "customer": "Dana", "amount": 110},
    {"id": 15, "customer": "Eli", "amount": 85},
    {"id": 16, "customer": "Aisha", "amount": 60},
    {"id": 17, "customer": "Ben", "amount": 95},
    {"id": 18, "customer": "Carlos", "amount": 75},
    {"id": 19, "customer": "Dana", "amount": 65},
    {"id": 20, "customer": "Eli", "amount": 115},
]

# Customers in the order they first appear
customers = list(dict.fromkeys(o["customer"] for o in orders))

# Total per customer: dict comprehension with a generator inside sum()
totals = {c: sum(o["amount"] for o in orders if o["customer"] == c) for c in customers}

print("Totals per customer:")
for customer, total in zip(totals.keys(), totals.values()):
    print(f"{customer}: {total}")

# Ranked highest to lowest: sorted() with a lambda key
ranked = sorted(totals.items(), key=lambda item: item[1], reverse=True)

print("\nRanking:")
for rank, (customer, total) in enumerate(ranked, start=1):
    print(f"{rank}. {customer} - {total}")

print("\nTop 3:")
print(ranked[:3])

# Average: generator expression inside sum()
average = sum(o["amount"] for o in orders) / len(orders)
print(f"\nAverage order: {average}")

# Orders above average: list comprehension
above = [o for o in orders if o["amount"] > average]
print(f"Orders above average: {[o['id'] for o in above]}")
print(f"Count above average: {len(above)}")


def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False


print("\nContains Duplicate tests:")
print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))