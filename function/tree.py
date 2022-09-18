def tree(root_laber, branches = []):
    for branch in branches:
        assert is_tree(branch)
    return [root_laber] + list(branches)

def laber(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) !=list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else :
        left,right = fib_tree(n-2), fib_tree(n-1)
        laber_n = laber(left) + laber(right)
        return tree(laber_n, [left, right])

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        brs = branches(tree)
        count_brs_leaves= [count_leaves(b) for b in brs]
        return sum(count_brs_leaves)

def partition_tree(n,m):
    if n == 0:
        return tree(True)
    elif n<0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m,m)
        right = partition_tree(n, m-1)
        return tree(m,[left, right])

def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if laber(tree):
            print("+".join(partition)) 
    else:
        m = str(laber(tree))
        left , right= branches(tree)
        print_parts(left,partition+[m])
        print_parts(right,partition)

"""next we define the linked list"""
empty = 'empty'
def is_link(s):
    return s == empty or (len(s)==2 and is_link(s[1]))
def link(first ,rest):
    assert is_link(rest)
    return [first, rest]

def first(s):
    assert is_link(s)
    assert s !=empty
    return s[0]

def rest(s):
    assert is_link(s)
    assert s !=empty
    return s[1]

def len_link(s):
    '''return the length of linked list s.'''
    length = 0
    while s != empty:
        s, length = rest(s) ,length +1
    return length

def getitem_link(s,i):
    while i >0:
        s, i = rest(s) , i -1
    return first(s)

def extend_link(s, t):
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s ) , extend_link(rest(s),t ))
def apply_to_all_link(f, s):
    if s==0:
        return s
    else:
        return link(f(first(s) ),apply_to_all_link(f,rest(s)))

four = [1,[2,[3,[4,'empty']]]]
def keep_if_link_ws(fliter, s,collect = []):
    if s == empty:
        collect = collect +[empty]
        return collect
    else:   
        if fliter(first(s)):
            collect = collect +[first(s )]
        return keep_if_link_ws(fliter ,rest(s ),collect )
def keep_if_link(fliter, s):
    if s == empty:
        return s
    else:
        kept = keep_if_link(fliter, rest(s))
        if fliter(first(s)):
            return link(first(s), kept)
        else:
            return kept
# b1 = keep_if_link_ws(lambda x : x%2 ==0 , four)
# b2 = keep_if_link(lambda x : x%2 ==0 , four)
# print(b1, b2)
def join_link(s, separator):
    if s == empty:
        return ''
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator +join_link(rest(s), separator)