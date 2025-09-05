class BankAccount:
    def __init__(self, owner, starting_balance):
        self.owner = owner
        self.balance = starting_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self, ):
        return self.balance
#example usage
acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())  

for item in dir(acc):
    if not item.startswith("__"):
        print(item)