class InvalidOrderError(Exception):
    """Raised when an order row is invalid."""
    pass


def validate_order(order):
    if "customer" not in order:
        raise InvalidOrderError("missing customer")
    if "amount" not in order:
        raise InvalidOrderError("missing amount")
    amount = order["amount"]
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise InvalidOrderError(f"amount is not a number: {amount!r}")
    if amount < 0:
        raise InvalidOrderError(f"amount is negative: {amount}")
    return float(amount)


orders = [
    {"id": 1, "customer": "Asha", "amount": 120.0},
    {"id": 2, "customer": "Ravi", "amount": 75.5},
    {"id": 3, "customer": "Asha"},
    {"id": 4, "customer": "Meera", "amount": "abc"},
    {"id": 5, "customer": "Ravi", "amount": None},
    {"id": 6, "customer": "Meera", "amount": -20},
    {"id": 7, "customer": "Asha", "amount": 30},
    {"id": 8, "customer": "Ravi", "amount": 24.5},
]

totals = {}
skipped = []
processed = 0

for order in orders:
    try:
        amount = validate_order(order)
    except InvalidOrderError as e:
        skipped.append((order.get("id", "?"), str(e)))
    else:
        customer = order["customer"]
        totals[customer] = totals.get(customer, 0.0) + amount
    finally:
        processed += 1

print("Good orders - totals per customer:")
for customer in sorted(totals):
    print(f"{customer}: {totals[customer]:.2f}")
print()
print(f"Processed {processed} orders")
print(f"Skipped {len(skipped)} bad orders:")
for order_id, reason in skipped:
    print(f"- order {order_id}: {reason}")
print()


def is_palindrome(s: str) -> bool:
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome(" "))