def greater_first(fun):
    def wrap(a,b):
        if a < b:
            a,b = b,a
        return fun(a,b)
    return wrap

@greater_first
def divide(a,b):
    return a / b

res1 = divide(3,4)
print(res1)

@greater_first
def sub(a,b):
    return a - b

res2 = sub(3,4)
print(res2)

