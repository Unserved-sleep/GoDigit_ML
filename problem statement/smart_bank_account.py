class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def __str__(self):
        return f"Balance: ${self.balance}"

    def withdraw(self,amount):
        try:
            if amount < self.balance:
                self.balance -= amount
                print(f"Withdraw Successful")
            else:
                raise Exception("InsufficientFundsError")

        except Exception as e:
            print(e)

    def deposit(self,amount):
        self.balance += amount

b  = BankAccount(100)
b.withdraw(150)
b.deposit(200)
print(b)
b.withdraw(150)
print(b)



