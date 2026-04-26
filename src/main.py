# To-do:
# - Create Split function

class Bill:
    def __init__(self, amount=0, persons=[], paied=False):
        self.amount = amount
        self.persons = persons
        self.paid = False
    
    def settle(self):
        self.paid = True
        return self.amount/len(set(self.persons))


def main():
    bill_01 = Bill(5, ['person1', 'person2'])
    print(bill_01.settle())


if __name__ == "__main__":
    main()