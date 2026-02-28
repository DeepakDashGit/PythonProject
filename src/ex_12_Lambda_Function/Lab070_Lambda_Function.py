def triple_number(num):
    return num * 3

result = triple_number(5)
print(result)

#lamda function
result_l_f = lambda num: num * 3  #num is argument and num*3 is return type
print(result_l_f(5))


result_mul = lambda a, b: a * b
print(result_mul(4, 5))


result_sum = lambda a, b, c: a + b + c
print(result_sum(4, 5, 6))

# lambda always returns a function so we need to call the function