import pytest

from playground.bank_account import BankAccount


@pytest.fixture
def bank_account():
    # Initialize a new BankAccount instance for each test.
    return BankAccount(100.00)


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
