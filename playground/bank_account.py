# playground/bank_account.py
class BankAccount:
    def __init__(self, initial_balance: float = 0.00) -> None:
        self.__balance: float = initial_balance

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient Funds")
        return self.__balance

    def get_balance(self) -> float:
        return self.__balance
