import csv
from collections import defaultdict

totals = defaultdict(float)
skipped = 0

with open("orders.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        customer = (row["customer"] or "").strip()
        amount_text = (row["amount"] or "").strip()

        if not customer or not amount_text:
            skipped += 1
            continue

        try:
            amount = float(amount_text)
        except ValueError:
            skipped += 1
            continue

        totals[customer] += amount

for customer, total in sorted(totals.items(), key=lambda item: item[1], reverse=True):
    print(f"{customer}: {total:.2f}")

print(f"Skipped bad rows: {skipped}")