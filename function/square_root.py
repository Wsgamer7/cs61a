
def square_root_update(a,x):
    return (a/x + x)/2

def condition(x, y, tolerance= 1e-15):
    return abs(x- y)< tolerance

def update_time(update, close, guess=1):
    while not close(guess):
        guess =update(guess)
    return guess

def square_root(a):
    def update(guess):
        return square_root_update(a,guess)
    def close(guess):
        return condition(guess*guess, a)
    return update_time(update, close)

print(square_root(4))