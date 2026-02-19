#  User defined function
#   1. non-return type
#   2. return type
#   3. default param
#   4. keyword
#   5. multiple param

#built-in function
resul = max(8,5)
print(resul)

#1. they can't return, no return type no parameter

def greet():
    print("hello")
greet()

#2. no return type with argument/parameter

def greet_by_name(name):
    print("Hi", name)
greet_by_name("Rasta")

#3. no return type with default argument

def say_hello_default_arg(name="Deepak"):
    print("Hello", name.upper())
say_hello_default_arg("Dash")
say_hello_default_arg()

#4. multiple arguments

def multiple_arguments(a, b, c):
    print("Hello", a, b, c)
multiple_arguments(1, 2, 3)

#5. argument with return type

def sum_of_two(a,b):
    return a + b
result = sum_of_two(10,20)
print(result)

def sum_of_two_numbers_default(d=100, e=200):
    print("Sum of the number is")
    return d + e
result = sum_of_two_numbers_default(d=25, e=25)
print(result)
result = sum_of_two_numbers_default()
print(result)





