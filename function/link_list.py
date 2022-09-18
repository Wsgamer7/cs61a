from calendar import c
from curses import flash
from queue import Empty
class Link:
    empty = ()
    def __init__(self,first, rest = empty):
        assert isinstance(rest,Link) or rest is self.empty
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)
    def __repr__(self):
        if self.rest == Link.empty:
            rest = ''
        else:
            rest = ', ' + repr(self.rest)
        return 'Link({0}{1})'.format(self.first, rest)
def extend_link(s,t):
    if s == Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))

def map_link(f, s):
    if s == Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f,s.rest))
def fliter_link(f,s):
    if s == Link.empty:
        return s
    else:
        if f(s.first):
            return Link(s.first, fliter_link(f, s.rest))
        else:
            return fliter_link(f, s.rest)

def join_link(separator, s):
    if s == Link.empty:
        return s 
    elif s.rest == Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(separator, s.rest)
def add_order(s,v):
    if s == Link.empty:
        return Link(v)
    elif s.rest == Link.empty and v > s.first:
        return Link(s.first, Link(v))
    else:
        if v< s.first:
            return Link(v,s)
        if v > s.first:
            return Link(s.first, add_order(s.rest, v))
class Tree:
    def __init__(self,laber, branches= []):
        self.laber = laber
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)
    def is_leaf(self):
        return not self.branches
    def __repr__(self):
        if self.branches:
            return 'Tree({0},{1})'.format(self.laber, repr(self.branches))
        else:
            return 'Tree({0})'.format(self.laber)

def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        laber = left.laber + right.laber
        return Tree(laber, [left,right])
def leaves(t):
    if t.is_leaf():
        return [t.laber]
    else:
        all_leaves = [ ]
        for branch in t.branches:
            all_leaves.extend(leaves(branch))
        return all_leaves
def set_contains(s,v):
    if s is None:
        return False
    elif s.entry == v:
        return True
    elif s.entry < v:
        return set_contains(s.right, v)
    elif s.entry >v :
        return set_contains(s.left, v)

def adjoin_set(s,v):
    if s is None:
        return Tree(v)
    elif s.entry == v:
        return s
    elif s.entry < v :
        return Tree(s.entry, s.left, adjoin_set(s.right, v ))
    elif s.entry > v:
        return Tree(s.entry,  adjoin_set(s.left, v ),s.right)
def empty(s):
    return s is Link.empty
def set_contains1(s,v):
    if empty(s ) or s.first > v:
        return False
    elif s.first == v:
        return True
    else:
        set_contains1(s.rest, v )

def intersect(set1,set2):
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        x1, x2 == set1.first, set2.first
        if x1 == x2:
            return Link(x1,intersect(set1.rest, set2.rest))
        elif x1 < x2:
            return intersect(set1.rest, set2)
        elif x1 > x2:
            return intersect(set1, set2.rest)


