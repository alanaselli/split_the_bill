# To-do:
# - Create a test for the Ledger class
# - Create the Ledger class

# For now, let's assume:
# - all bills are split equally
# - only two people are involved

class Bill:
    def __init__(self, amount=0, paid_by=None):
        self.amount = amount
        self.paid_by = paid_by

        self.receives = self.amount/2

def main():
    bill_01 = Bill(5, paid_by='person1')
    print("Amount: ", bill_01.amount)
    print("Paid by: ", bill_01.paid_by)
    print("Receives: ", bill_01.receives)


if __name__ == "__main__":
    main()