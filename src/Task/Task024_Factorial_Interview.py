def factorial(num):
    if not isinstance(num,int):
        return None
    if num < 0:
        return None
    result = 1
    for i in range(1,num+1):
        result = result * i
    return result
pass
print(factorial(5))
