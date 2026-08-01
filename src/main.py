# For now, let's assume:
# - all bills are split equally
# - only two people are involved

class Bill:
    def __init__(self, amount=0, paid_by=None, shared_with=None, is_settled=False):
        self.amount = amount
        self.paid_by = paid_by
        self.shared_with = shared_with
        self.is_settled = is_settled

    def _calculate_receives(self):
        self._receives = self.amount/2
    
    def _settle(self):
        self.is_settled = True

class Ledger:
    def __init__(self):
        self.list_of_bills = []
        self.balance = {}

    def add_bill(self, bill):
        bill._calculate_receives()
        self.list_of_bills.append(bill)

    def calculate_balances(self):

        for bill in self.list_of_bills:
            if not bill.is_settled:
                self.balance.setdefault(bill.paid_by, 0)
                self.balance.setdefault(bill.shared_with, 0)
                # setdefault() returns the value of a specified key if it exists.
                # If the key does not exist, it adds the key with a default value and returns that default.

                self.balance[bill.paid_by] += bill.amount/2
                self.balance[bill.shared_with] -= bill.amount/2

    def settle_up(self):
        for bill in self.list_of_bills:
            bill._settle()


def main():
    bill_01 = Bill(5, paid_by='person1', shared_with='person2')
    print("Amount: ", bill_01.amount)
    print("Paid by: ", bill_01.paid_by)
    print("Shared with: ", bill_01.shared_with)
    print("Receives: ", bill_01.receives)


if __name__ == "__main__":
    main()