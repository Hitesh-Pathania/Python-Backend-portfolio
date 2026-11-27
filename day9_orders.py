from dataclasses import dataclass


@dataclass
class Order:
    id: int
    customer: str
    amount: float

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")

    def __lt__(self, other):
        return self.amount < other.amount


def totals_per_customer(orders):
    totals = {}
    for order in orders:
        totals[order.customer] = totals.get(order.customer, 0) + order.amount
    return totals

orders = [
    Order(1, "Hitesh", 150.0),
    Order(2, "Shivali", 100.0),
    Order(3, "Hitesh", 50.0),
    Order(4, "Rithik", 200.0),
    Order(5, "Hitesh", 25.0),
]

print("Orders sorted by amount:")
for order in sorted(orders):
    print(order)

print()
print("Totals per customer:")
for customer, total in totals_per_customer(orders).items():
    print(f"{customer}: {total:.2f}")