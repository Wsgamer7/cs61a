# def summation(n, term):
#     k, total = 1, 0
#     while k <= n:
#         k, total = k+1, total + term(k)
#     return total
# def cubes(x):
#     return x*x*x
# # print(summation(5,cubes)  ) 
# def pi_sum(x):
#     return 8/((4*x - 3)*(4*x -1))
# a  = summation(8000,pi_sum)
# print(a)

def improve(update, close , guess = 1):
    while not close(guess):
        guess= update(guess)
    return guess
def golden_update(x):
    return - 3 - 1/x
def approx_eq(x,y, tolerance = 1e-7):
    return abs(x - y)<tolerance
def golden_close(guess):
    return approx_eq(guess, -3 - 1/guess)

b = improve(golden_update, golden_close)
print(b)

def average(x,y):
    return (x+y)/2

def sqrt_update(x,a):
    return average(x, a/x)

def sqrt_ws(a):
    def update(x):
        return sqrt_update(x,a)
    def close(x):
        return approx_eq(x*x, a)
    return improve(update, close)

print(sqrt_ws(3))
