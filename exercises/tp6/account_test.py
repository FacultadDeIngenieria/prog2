import unittest

from account import (Account, Owner)

moe: Owner = Owner(1, "Moe")
larry: Owner = Owner(2, "Larry")
curly: Owner = Owner(10, "Curly")

class AccountTest(unittest.TestCase):

    def test_creation_owner(self):
        self.assertEqual("Moe", moe.name)

    def test_creation_account(self):
        moe_account = Account(1, moe)
        self.assertEqual(1, moe_account.account_number)
        self.assertEqual(1, moe_account.owner.id_number)
        self.assertEqual("Moe", moe_account.owner.name)
        self.assertEqual(0.0, moe_account.get_balance())

    def test_deposit(self):
        moe_account = Account(1, moe)
        moe_account.deposit(100)
        self.assertEqual(100, moe_account.get_balance())

    def test_withdraw(self):
        moe_account = Account(1, moe)
        moe_account.deposit(100)
        moe_account.withdraw(50)
        self.assertEqual(50, moe_account.get_balance())

    def test_transfer(self):
        moe_account = Account(1, moe)
        larry_account = Account(2, larry)
        moe_account.deposit(100)
        moe_account.transfer(30, larry_account)
        self.assertEqual(70, moe_account.get_balance())
        self.assertEqual(30, larry_account.get_balance())

    def test_list_accounts(self):
        moe_account = Account(1, moe)
        larry_account = Account(2, larry)
        curly_account = Account(3, curly)
        self.assertEqual([moe_account, larry_account, curly_account], Account.get_accounts())

    def test_access_account(self):
        Account(1, moe)
        Account(2, larry)
        Account(3, curly)
        self.assertEqual("Curly", Account.get_account(3).owner.name)

    def test_transactions(self):
        moe_account = Account(1, moe)
        larry_account = Account(2, larry)
        moe_account.deposit(100)
        moe_account.transfer(30, larry_account)
        moe_account.withdraw(40)
        self.assertEqual(30, moe_account.get_balance())
        transactions = moe_account.get_transactions()
        self.assertEquals(3, len(transactions))
        amounts = [t.amount for t in transactions]
        self.assertEquals([100, 30, 40], amounts)
