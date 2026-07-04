# To-do:
# - Create a test for the Ledger class
# - Create the Ledger class

# For now, let's assume:
# - all bills are split equally
# - only two people are involved

class Bill:
    def __init__(self, amount=0, paid_by=None, shared_with=None, is_settled=False):
        self.amount = amount
        self.paid_by = paid_by
        self.shared_with = shared_with
        self.is_settled = is_settled

        self.receives = self.amount/2
    
    def settle(self):
        self.is_settled = True

class Ledger:
    def __init__(self):
        self.list_of_bills = []
        self.balance = {}

    def add_bill(self, bill):
        self.list_of_bills.append(bill)

    def get_balances(self):

        for bill in self.list_of_bills:
            self.balance.setdefault(bill.paid_by, 0)
            self.balance.setdefault(bill.shared_with, 0)

            self.balance[bill.paid_by] += bill.amount/2
            self.balance[bill.shared_with] -= bill.amount/2


def main():
    bill_01 = Bill(5, paid_by='person1', shared_with='person2')
    print("Amount: ", bill_01.amount)
    print("Paid by: ", bill_01.paid_by)
    print("Shared with: ", bill_01.shared_with)
    print("Receives: ", bill_01.receives)


if __name__ == "__main__":
    main()