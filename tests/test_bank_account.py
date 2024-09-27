# tests/test_bank_account.py
import pytest

from playground.classes.bank_account import BankAccount


@pytest.fixture
def bank_account():
    # Initialize a new BankAccount instance for each test.
    return BankAccount(name="Richard Beninya", account_id=666, initial_balance=100.00)


def test_get_balance(bank_account):
    assert bank_account.get_balance() == 100.00


def test_deposit(bank_account):
    bank_account.deposit(50.00)
    assert bank_account.get_balance() == 150.00


def test_withdraw(bank_account):
    bank_account.withdraw(50.00)
    assert bank_account.get_balance() == 50.00


def test_withdraw_insufficient_funds(bank_account):
    with pytest.raises(ValueError, match="Insufficient Funds"):
        bank_account.withdraw(200.00)


def test_withdraw_to_exact_zero(bank_account):
    bank_account.withdraw(100.00)
    assert bank_account.get_balance() == 0.00


def test_deposit_zero(bank_account):
    bank_account.deposit(0.00)
    assert bank_account.get_balance() == 100.00


def test_deposit_negative_amount(bank_account):
    with pytest.raises(ValueError):  # Assuming your implementation should handle this
        bank_account.deposit(-10.00)


def test_multiple_transactions(bank_account):
    bank_account.deposit(50.00)
    bank_account.withdraw(25.00)
    bank_account.deposit(10.00)
    assert bank_account.get_balance() == 135.00


def test_large_deposit_withdrawal(bank_account):
    bank_account.deposit(1_000_000.00)
    assert bank_account.get_balance() == 1_000_100.00
    bank_account.withdraw(1_000_000.00)
    assert bank_account.get_balance() == 100.00
