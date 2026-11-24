class TransactionLog:
    def __init__(self):
        self.entries=[]

    def record(self, entry):
        self.entries.append(entry)

    def show(self):
        for entry in self.entries:
            print(f"-{entry}")

class account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        self.log = TransactionLog()
        self.log.record(f"Account opened with ${balance:.2f}")

    def deposit(self, amount):
        self.balance +=amount
        self.log.record(f"Desposited ${amount: .2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal failed: not enough money in the account.")
            return False
        self.balance -= amount
        self.log.record(f"Withdrew ${amount:.2f}")
        return True

class savingsaccount(account):
    def __init__(self, owner, balance=0, interest_rate = 0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance*self.interest_rate
        self.balance += interest
        self.log.record(f"Interest added: ${interest:.2f}")

class currentaccount(account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            print("Withdrawal failed: that would pass the overdraft limit.")
            return False
        self.balance -= amount
        self.log.record(f"Withdrew ${amount:.2f}")
        return True

savings = savingsaccount("Hitesh", 200, 0.05)
savings.deposit(50)
savings.add_interest()
print(f"{savings.owner}'s savings balance: ${savings.balance:.2f}")
print("Transactions:")
savings.log.show()

current = currentaccount("Shivali", 80, 100)
current.withdraw(150)
current.withdraw(50)
print(f"{current.owner} current balance: ${current.balance:.2f}")
print("Transactions:")
current.log.show()
