from traceback import print_tb
from link_list import *
a = Link(1,Link(2))
squre = lambda x : x*x
m_a = map_link(squre, a)
print(m_a)