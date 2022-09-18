from math import lgamma


higer_order_lambda = lambda f : lambda x : f(x)
g = lambda x : x*x
higer_order_lambda(2)(g)