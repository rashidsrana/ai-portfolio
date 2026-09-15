from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # encapsulated attribute

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self._balance

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def account_type(self):
        pass
