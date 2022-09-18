def compose_all(lst):
    if len(lst)== 1:
        return lst[0]
    elif len(lst) > 1:
        def help(x):
            return lst[1](lst[0](x))
        new_lst = [help] + lst[2:]
        return compose_all(new_lst)
def square(x):
    return x*x
def nagative(x):
    return -x
def sum1(x):
    return x + 1
def insert(x):
    return x
compose1 = compose_all([square, nagative])
print(compose1(1))
def compose(lst):
    if not lst:
        return insert
    else:
        def help(x):
            return compose(lst[1:])(lst[0](x))
        return help

compose2 = compose([square, nagative])
print(compose2(1))

