import unittest  # https://docs.python.org/3/library/unittest.html

from src.main import Bill, Ledger

class TestBill(unittest.TestCase):
    def test_default_amount(self):
        bill = Bill()
        self.assertEqual(bill.amount, 0)
    
    def test_amount(self):
        bill = Bill(1)
        self.assertEqual(bill.amount, 1)

    def test_division(self):
        bill = Bill(50, "Person A")
        self.assertEqual(bill.receives, 25)

    def test_is_settled_default(self):
        bill = Bill()
        self.assertFalse(bill.is_settled)

    def test_is_settled(self):
        bill = Bill()
        bill.settle()
        self.assertTrue(bill.is_settled)

class TestLedger(unittest.TestCase):
    def test_add_bill(self):
        bill = Bill(amount=50, paid_by="Person A", shared_with="Person B")
        
        ledger = Ledger()
        ledger.add_bill(bill)

        self.assertListEqual(ledger.list_of_bills, [bill])

    def test_get_balances(self):
        bill = Bill(amount=50, paid_by="Person A", shared_with="Person B")

        ledger = Ledger()
        ledger.add_bill(bill)

        ledger.get_balances()

        self.assertDictEqual(ledger.balance, {"Person A": 25, "Person B": -25})

    def test_get_balances_2(self):
        bill_01 = Bill(amount=50, paid_by="Person A", shared_with="Person B")
        bill_02 = Bill(amount=20, paid_by="Person B", shared_with="Person A")

        ledger = Ledger()
        ledger.add_bill(bill_01)
        ledger.add_bill(bill_02)

        ledger.get_balances()

        self.assertDictEqual(ledger.balance, {"Person A": 15, "Person B": -15})

    def test_get_balances_twice(self):
        # Test whether calling get_balances() twice the balances do not double

        bill_01 = Bill(amount=50, paid_by="Person A", shared_with="Person B")

        ledger = Ledger()
        ledger.add_bill(bill_01)

        ledger.get_balances()
        balance_1 = ledger.balance
        
        ledger.get_balances()
        balance_2 = ledger.balance

        self.assertEqual(balance_1, balance_2)

if __name__ == "__main__":
    unittest.main()