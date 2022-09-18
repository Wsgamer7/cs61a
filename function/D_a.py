def rational(x,y):
    return [x, y]
def numer(x):
    return x[0]
def deno(x):
    return x[1]
def mul_rational(x,y):
    return rational(numer(x) * numer(y),deno(x) * deno(y))

def add_rational(x,y):
    return rational(numer(x) * deno(y) + numer(y)*deno(x) , deno(x)*deno(y))
def nag_rational(x,y):
    return rational(numer(x) * deno(y) - numer(y)*deno(x) , deno(x)*deno(y))

def div_rational(x, y):
    return rational(numer(x) *deno(y) ,deno(x)*numer(y))

def is_eq_rational(x,y):
    return numer(x) * deno(y) == deno(x) * numer(y)

def print_rational(x):
    print(numer(x), "/", deno(x))
