# from hw02 import count_coins
# i = count_coins(15)
# print("time is", i)


def deco(f):
    def wrap(x):
        print(x, "->")
        return f(x)
    return wrap


@deco
def squares(x):
    return x*x
squares(2)