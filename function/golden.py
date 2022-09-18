def improve(update, close, guess =1):
    while not close(guess):
        guess = update(guess)
    return guess
def golden_update(x):
    return 1+1/x
def golden_close(x ,tolerance=1e-10):
    return abs(x*x-x-1) < tolerance
re=improve(golden_update , golden_close)
print(re)