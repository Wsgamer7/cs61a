from re import X
from operator import add,mul

def divisors(n):
    return [1] + [x for x in range(2,n) if n%x ==0]

def width(area, height):
    assert area % height == 0
    return area // height
def perimeter(width , height):
    return 2*(width + height)

def minimum_perimeter(area):
    height = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in height]
    return min(perimeters)

def apply_to_all(map_f, s):
    return [map_f(x) for x in s]

def keep_if(filter, s):
    return [x for x in s if filter(x)]
    
def reduce(reduce_f, s, initial):
    reduced = initial
    for x in s :
        reduced = reduce_f(reduced , x)
    return reduced

def devisors_of(n):
    devisors_n = lambda x : n%x == 0
    devisors = keep_if(devisors_n, range(2,n))
    return [1] + devisors

def sum_of_devisors(n):
    return reduce(add, devisors_of(n), 0)

def prefect(n):
    return sum_of_devisors(n)== n

a = keep_if(prefect, range(1,1000))
print(a)
print(sum_of_devisors(12))