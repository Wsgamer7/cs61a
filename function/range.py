def sum_below(n):
    """1+2+...+n-1"""
    total =1
    for i in range(n):
        total += i
    return total

def cheer(n):
    for _ in range(n):
        print("cheer! ws")

def divisors(n):
    return [1] + [x for x in range(2,n) if n % x ==0]
