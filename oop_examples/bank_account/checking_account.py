from account import Account


class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=200):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        self._balance -= amount
        return self._balance

    def account_type(self):
        return "Checking Account"
