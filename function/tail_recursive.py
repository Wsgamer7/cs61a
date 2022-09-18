def factorial(n, k):
    '''
    Compute n! * k
    '''
    if n == 0:
        return k
    else:
        return factorial(n-1, n*k)
def factorial2(n, k):
    """
    Compute n! * k
    >>> factorial2(3,1)
    3
    """
    result = k
    if n == 0:
        return result
    else:
        for i in range(2, n +1):
            result = result* i
        return result
