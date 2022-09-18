def count(s, value):
    """ count the times of value in s
    >>> count([2,3,5,4,6,6,6,9], 6)    
    3                                  
            """
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index +1
    return total

def same_count(s):
    total = 0
    for x, y,z in s:
        if x == y == z:
            total = total +1
    return total
