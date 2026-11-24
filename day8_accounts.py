class TransactionLog:     # Its only job is to remember account activity.
    def __init__(self):        
        self.entries=[]   # Create an empty list called entries.
        # This list will store messages like "Deposited $50.00".

    def record(self, entry):
        self.entries.append(entry)   # Add one entry/message into the entries list.

    def show(self):
        for entry in self.entries:      # Loop through all entries.
            print(f"-{entry}")          # Print each entry one by one.


# Account is the parent/base class.
# SavingsAccount and CurrentAccount will inherit from this.
class account:
    def __init__(self, owner, balance = 0):
        self.owner = owner              # Store the owner's name.
        self.balance = balance          # Store the starting balance.
        self.log = TransactionLog()     # Create a TransactionLog object and store it as self.log.
        self.log.record(f"Account opened with ${balance:.2f}")            # Record the first message: account opened with starting balance.

    def deposit(self, amount):
        self.balance +=amount         # Add amount to balance
        self.log.record(f"Desposited ${amount: .2f}")           # Record this deposit in the log.

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal failed: not enough money in the account.")                     # First check: if amount is bigger than balance, refuse.
            return False
        self.balance -= amount                                                               # Otherwise subtract amount from balance.
        self.log.record(f"Withdrew ${amount:.2f}")                                           # Record this withdrawal in the log.
        return True


# SavingsAccount inherits from Account.
class savingsaccount(account):
    def __init__(self, owner, balance=0, interest_rate = 0.02):
        super().__init__(owner, balance)                    # First call super().__init__ to let Account set up owner and balance
        self.interest_rate = interest_rate                  # Then store interest_rate as this savings account's special data.

    def add_interest(self):
        interest = self.balance*self.interest_rate          # Calculate interest: balance multiplied by interest_rate.
        self.balance += interest                            # Add that interest to balance.
        self.log.record(f"Interest added: ${interest:.2f}")    # Record the interest in the log.


# CurrentAccount also inherits from Account.
class currentaccount(account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)                       # First call super().__init__ to let Account set up owner and balance.
        self.overdraft_limit = overdraft_limit                 # Then store overdraft_limit.

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            print("Withdrawal failed: that would pass the overdraft limit.")           # Check if balance - amount goes below -overdraft_limit.
            return False
        self.balance -= amount                                                          # Otherwise subtract amount, record it, and return True.
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
