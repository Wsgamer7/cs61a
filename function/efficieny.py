def fib(n):
    if n == 0 or n ==1 :
        return n
    else:
        return fib(n-2) + fib(n-1)

def count(f):
    def counted(*arg):
        counted.called_count += 1
        return f(*arg)
    counted.called_count = 0
    return counted

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

def square(x):
    return x*x
@count
def exponent(x,n):
    if n == 0:
        return 1
    elif n %2 == 1:
        return x * exponent(x,n-1)
    elif n %2 == 0:
        return square(exponent(x, n//2))
@count
def exponent1(x,n):
    if n == 0:
        return 1
    else:
        return x * exponent1(x, n-1)
