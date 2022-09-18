def count_stair_ways(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else :
        return count_stair_ways(n-1) + count_stair_ways(n-2)
def square(x):
    return x*x

li = [square(x) for x in [1,3,5,6,4,8] if x%2==1]
print(li)
