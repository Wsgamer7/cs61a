def trace(f):
    def wrapped(x):
        print('->', f,'(',x, ')')
        return f(x)
    return wrapped
s = lambda x : x*x*x
print(trace(s)(2))