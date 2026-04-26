import unittest  # https://docs.python.org/3/library/unittest.html

from src.main import Bill

class TestBill(unittest.TestCase):
    def test_default_amount(self):
        bill = Bill()
        self.assertEqual(bill.amount, 0)
    
    def test_amount(self):
        bill = Bill(1, ['person1', 'person2'])
        self.assertEqual(bill.amount, 1)

    def test_default_persons(self):
        bill = Bill()
        self.assertEqual(bill.persons, [])

    def test_count_persons(self):
        bill = Bill(1, ['person1', 'person2', 'person3'])
        self.assertEqual(len(bill.persons), 3)
    
    def test_default_paied(self):
        bill = Bill()
        self.assertFalse(bill.paid)

    def test_paied(self):
        bill = Bill(2, ['person1', 'person2'])
        bill.settle()
        self.assertTrue(bill.paid)

if __name__ == "__main__":
    unittest.main()