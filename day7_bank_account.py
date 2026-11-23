class bankaccount:
    # It stores the starting data (owner and balance) on the object
    def __init__(self, owner, balance):
        self.owner = owner      # remember who this account belongs to
        self.balance = balance  # remember how much money it starts with


    def deposit(self, amount):
        # reject zero or negative amounts
        if amount  <= 0:
            print("Deposit amount must be positive")
            return
        # Add the money to this account's balance
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        # reject zero or negative amounts
        if amount <= 0:
            print("Withdraw amount must be positive.")
            return
        #reject if trying to take out more than the balance
        if amount > self.balance:
            print("Insufficient Funds")
            return
        # Both checks passed: subtract the money from the balance
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")

    # __repr__ controls what you see when you print() an account object
    # Without it, Python prints a useless memory address instead
    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance:.2f})"

acc1 = bankaccount("Hitesh", 100)
acc2 = bankaccount("Shivali", 50)
print(acc1)
print(acc2)
acc1.deposit(50)
acc1.withdraw(30)
acc1.withdraw(200)
acc2.deposit(25)
acc2.withdraw(10)
print(acc1)
print(acc2)