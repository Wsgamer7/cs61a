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
def account(initial_balance):
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']
    dispatch = {'deposit':   deposit,
                'withdraw':  withdraw,
                'balance':   initial_balance}
    return dispatch

def withdraw(account, amount):
    return account['withdraw'](amount)
def deposit(account, amount):
    return account['deposit'](amount)
def check_balance(account):
    return account['balance']

a  = Account('ws')
# a.deposit(100)
# print(type(a.balance),type(a.deposit))
# print(type(Account.deposit))
# b = account(0)
# b['deposit'](100)
# print(type(b['deposit']), b['balance'])
a.interest = 0.04
b = Account('ws')
Account.interest = 0.09
print(a.interest,b.interest)