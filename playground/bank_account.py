# playground/bank_account.py
class BankAccount:
    def __init__(self, initial_balance: float = 0.00) -> None:
        self.balance: float = initial_balance

    def deposit(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Funds")
        return self.balance

    def get_balance(self) -> float:
        return self.balance
