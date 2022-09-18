
try:
    x = 1/0
except ZeroDivisionError as e:
    print('has a', type(e))
    x = 0
def invent_safe(x):
    try:
        aim = 1 / x
        return aim
    except ZeroDivisionError as e:

        return str(e)
class IterImproveError(Exception):
    def __init__(self, last_guess):
        self.last_guess = last_guess

def improve(update, done , guess =1 , max_update = 1000):
    k = 0
    try:
        while not done(guess) and k < max_update:
            guess = update(guess)
            k += 1
        return guess
    except ValueError:
        raise IterImproveError(guess)
def newton_update(f, df):
    def update(x):
        x = x - f(x)/df(x)
        return x
    return update

def find_zero(f,df, guess = 1):
    def done(x):
        return abs(f(x)) < 0.000001
    try:
        return improve(newton_update(f, df), done, guess)
    except IterImproveError as e:
        return e.last_guess
from math import sqrt
def f(x):
    return 2*x*x + sqrt(x)
def df(x):
    return 4*x + (1/2)*(1 / sqrt(x))
print(find_zero(f, df))