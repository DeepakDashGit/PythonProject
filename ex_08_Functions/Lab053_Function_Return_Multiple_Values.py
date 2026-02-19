#function returns multiple values

def math_operation(num1, num2):
    return num1 + num2, num1 * num2, num1 - num2

sum_n, mul_n, dif_n = math_operation(8, 3)
print(sum_n, mul_n, dif_n)
print(mul_n)
print(dif_n)

