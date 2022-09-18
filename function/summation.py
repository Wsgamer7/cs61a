from tkinter import E


def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x

def indentity(x):
    return x

def sum_square(n):
    return summation(n, square)

text = summation(100, square)
print(text)