def print_delay(n):
    def print_1(k):
        print(n)
        return print_delay(k)
    return print_1

f = print_delay(1)
f = f(3)
f = f(4)
def likes(n):
    """Return whether George Boole likes the non-negative inter n"""
    