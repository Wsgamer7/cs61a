# def map_to_range(start, end , f):
#     while start<= end :
#         print(f(start))
#         start= start +1
#     return start

# def curried_pow(x):
#     def h(y):
#         return pow(x, y)
#     return h
# map_to_range(1,10,curried_pow(2))

# def curry2(f):
#     def g(x):
#         def h(y):
#             return f(x,y)
#         return h
#     return g

# map_to_range(1, 10 , curry2(pow)(2))

from re import X


def square(x):
    return x*x

def cubes(x):
    return x*x*x

def compose_1(f,g):
    def intermediate(x):
        return f(g(x))
    return intermediate

a1= compose_1(cubes, square)
print(a1(2))

def compose_b1(f,g):
    return lambda x : f(g(x))   
a2 = compose_b1(cubes ,square)
print (a2(2))

s = lambda x : cubes(square(x))
print(s(2))

a3 = compose_b1(lambda x : x*x*x, lambda y : y+1)
print(a3(1))