def square(x):
    return x * x
def apply_twice(f,x):
    return f(f(x))

print(square(2))    
print(apply_twice(square, 2))
def improve(update, close , guess = 1):
    while not close(guess):
        guess= update(guess)
    return guess

def update_newton(f , df):
    def update(x):
        return x - f(x)/df(x)
    return update

def approx_eq(x,y, tolerance = 1e-7):
    return abs(x - y)<tolerance

def find_zeros(f, df):
    def close_zero(guess):
        return approx_eq(0, f(guess))
    return improve(update_newton(f,df), close_zero)

def square_root_newtoon(a):
    def df(x):
        return 2*x
    def f(x): 
        return x*x-a
    return find_zeros(f,df )

m=square_root_newtoon(4)
print(m)