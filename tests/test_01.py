import unittest  # https://docs.python.org/3/library/unittest.html

from src.main import Bill

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

if __name__ == "__main__":
    unittest.main()