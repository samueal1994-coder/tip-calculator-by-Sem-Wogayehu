# accounts.py

class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds or invalid withdrawal amount")

    def statement(self):
        return f"Account ({self.owner}): Balance = {self.balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, owner, balance=0.0, rate=0.02):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.balance += self.balance * self.rate

    def statement(self):
        return f"SavingsAccount ({self.owner}): Balance = {self.balance:.2f}"


class CurrentAccount(Account):
    def __init__(self, owner, balance=0.0, overdraft=500.0):
        super().__init__(owner, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance + self.overdraft:
            self.balance -= amount
        else:
            raise ValueError("Withdrawal exceeds overdraft limit")

    def statement(self):
        return f"CurrentAccount ({self.owner}): Balance = {self.balance:.2f}"


if __name__ == "__main__":
    accounts = [
        SavingsAccount("Alice", 1000, rate=0.05),
        CurrentAccount("Bob", 500, overdraft=300),
        Account("Charlie", 200)
    ]

    # Apply interest to savings
    accounts[0].add_interest()

    # Withdraw from current account
    accounts[1].withdraw(600)

    # Polymorphic loop
    for acc in accounts:
        print(acc.statement())
