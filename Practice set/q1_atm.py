class Atm:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def withdraw(self, amount):
        status = lambda x: "Success" if amount%100 == 0 and self.balance >= amount else "Failed"
        return status(amount)

init_balance: int = int(input())
n = int(input())
atm = Atm(init_balance)
for _ in range(n):
    with_amount = int(input())
    print(atm.withdraw(with_amount))