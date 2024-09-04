from playground.bank_account import BankAccount

bank_account = BankAccount(100.00)


def test_get_balance():
    assert bank_account.get_balance() == 100.00
