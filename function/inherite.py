
class Account:
    interest = 0.02
    def __init__(self, holder):
        self.balance = 0
        self.holder = holder
    def withdraw(self, amount):
        if amount > self.balance:
            print('insuffie balance')
        else:
            self.balance = self.balance - amount
        return self.balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def holder(self):
        return self.holder
    def nbalance(self):
        return self.balance 

class CheckingAccount(Account):
    interest = 0.01
    withdraw_charge = 1
    def withdraw(self, amount):
        return Account.withdraw(self, amount+ self.withdraw_charge)

class SavingAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)
class HybirdsAccount(CheckingAccount, SavingAccount):
    def __init__(self, holder):
        self.balance = 1
        self.holder = holder
a = HybirdsAccount('ws')
a.deposit(10)
a.withdraw(1)
print(a.balance)