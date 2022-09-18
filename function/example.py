import random
from this import d
from unittest import result
def rand_list(start, end, n):
    """Return a Random list of lenth n that contains random number in range(start, end)"""
    i, result = 0 , []
    for i in range(n):
        added = random.randrange(start, end)
        result.append(added)
    return result
def digit_dict(lst):
    return {d : [x for x in lst if x % 10 == d] for d in range(10) if [x % 10 == d for x in lst]}

def ordered(s, key = lambda x:x):
    if s == Link.empty or s.rest == Link.empty:
        return True
    elif key(s.first) < key(s.rest.first):
        return ordered(s.rest)
    else:
        return False

def merge(s, t):
    '''Return a sorted link list containing all entries in lnk s and t ordered'''
    if s == Link.empty:
        return t
    elif t == Link.empty:
        return s
    else:
        if s.first <= t.first:
            return Link(s.first, merge(s.rest, t))
        else:
            return Link(t.first, merge(s, t.rest))

def merge_in_place(s, t):
    '''Return a sorted link list containing all entries in lnk s and t ordered'''
    if s == Link.empty:
        return t
    elif t == Link.empty:
        return s
    else:
        if s.first <= t.first:
            s.rest = merge_in_place(s.rest, t)
            return s
        else:
            t.rest = merge_in_place(s, t.rest)
            return s
def increasing(n, biggest = 10):
    '''
    Return the largest sequence of digits with in n that is increasing.
    >>>increasing(124692)
    12469
    '''
    if n < 10 :
        return n
    elif n % 10 <= biggest:
        yes = increasing(n//10, n%10)*10 + n%10
        no = increasing(n//10, biggest)
        return max(yes, no)
    else:
        return increasing(n//10, biggest)
print(increasing(124692))