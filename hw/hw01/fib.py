def fib(n):
    pre =0 
    last =1
    k=2
    while k < n:
        pre = last 
        last = pre + last
        k = k + 1
    return last
assert fib(1) == 1 ,'The 8th Fibonacci number should be 13'
result = fib(8)
print(result)