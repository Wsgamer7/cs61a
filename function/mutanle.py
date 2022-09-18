from datetime import  date
tues = date(2022, 7, 30)
# print(tues.year)
# print(tues - date(2000,4, 12))
# print(tues)
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        else:
            balance = balance - amount
            return  balance
    return withdraw
withdraw= make_withdraw(100)
print(withdraw(25))
print(withdraw(25))

withdraw1= make_withdraw(100)
print(withdraw1(25))
print(withdraw(25))