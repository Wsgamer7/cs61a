def double(x):
    print('**',x,'-->',x*2,'**')
    return x*2
def even(start,end):
    even = start + start%2
    while even<end:
        yield even
        even += 2
def even1(start,end):
    even1= start + start%2
    lst =[]
    while even1<end:
        lst.append(even1)
        even1 +=2
    return lst
def a_then_b(a,b):
    for i in a:
        yield i
    for i in b:
        yield i
def countdown(x):
    if x > 0:
        yield x
        yield from countdown(x-1)
print(list(countdown(4)))
def prefix(s):
    if s:
        yield from prefix(s[:-1])
        yield s
tex = prefix('name')
print(list(tex))
def substring(s):
    if s:
        yield from prefix(s)
        yield from substring(s[1:])

class Account:
    def __init__(self , account_holder):
        self.balance = 0
        self.holder = account_holder
# a = Account('wangshuo')
# b = Account('lyf')
# b.balance = 200
# bal_list = [acc.balance for acc in [a,b]]
# print(bal_list)
a= [1,2]
a.pop(0)
print(a)