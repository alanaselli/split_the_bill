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
        bill._calculate_receives()
        self.assertEqual(bill._receives, 25)

    def test_is_settled_default(self):
        bill = Bill()
        self.assertFalse(bill.is_settled)

    def test_is_settled(self):
        bill = Bill()
        bill._settle()
        self.assertTrue(bill.is_settled)

class TestLedger(unittest.TestCase):
    def test_add_bill(self):
        bill = Bill(amount=50, paid_by="Person A", shared_with="Person B")
        
        ledger = Ledger()
        ledger.add_bill(bill)

        self.assertListEqual(ledger.list_of_bills, [bill])

    def test_calculate_balances(self):
        bill = Bill(amount=50, paid_by="Person A", shared_with="Person B")

        ledger = Ledger()
        ledger.add_bill(bill)

        ledger.calculate_balances()

        self.assertDictEqual(ledger.balance, {"Person A": 25, "Person B": -25})

    def test_calculate_balances_2(self):
        bill_01 = Bill(amount=50, paid_by="Person A", shared_with="Person B")
        bill_02 = Bill(amount=20, paid_by="Person B", shared_with="Person A")

        ledger = Ledger()
        ledger.add_bill(bill_01)
        ledger.add_bill(bill_02)

        ledger.calculate_balances()

        self.assertDictEqual(ledger.balance, {"Person A": 15, "Person B": -15})

    def test_calculate_balances_twice(self):
        # Test whether calling calculate_balances() twice the balances do not double.

        bill_01 = Bill(amount=50, paid_by="Person A", shared_with="Person B")

        ledger = Ledger()
        ledger.add_bill(bill_01)

        ledger.calculate_balances()
        balance_1 = ledger.balance
        
        ledger.calculate_balances()
        balance_2 = ledger.balance

        self.assertEqual(balance_1, balance_2)

    def test_calculate_balances_with_settled_bills(self):
        # Test whether a settled bill is excluded from the balances.

        bill_01 = Bill(amount=50, paid_by="Person A", shared_with="Person B", is_settled=True)
        bill_02 = Bill(amount=20, paid_by="Person B", shared_with="Person A")

        ledger = Ledger()
        ledger.add_bill(bill_01)
        ledger.add_bill(bill_02)

        ledger.calculate_balances()
        balance = ledger.balance

        self.assertDictEqual(balance, {"Person B": 10, "Person A": -10})

    def test_settle_up(self):
        bill_01 = Bill(amount=50, paid_by="Person A", shared_with="Person B", is_settled=True)
        bill_02 = Bill(amount=20, paid_by="Person B", shared_with="Person A")

        ledger = Ledger()
        ledger.add_bill(bill_01)
        ledger.add_bill(bill_02)

        ledger.settle_up()

        ledger.calculate_balances()

        self.assertDictEqual(ledger.balance, {})

if __name__ == "__main__":
    unittest.main()