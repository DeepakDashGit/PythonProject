# square of numbers

digits = [1, 2, 3, 4, 5]

def squ(x):
    return x ** 2
square_of_numbers = list(map(squ, digits))
print(square_of_numbers)

# list to upper case

name = ["House", "Building", "Room", "Roof"]
def upper_case(string):
    return string.upper()
result = list(map(upper_case, name))
print(result)

# convert time to millisecond

response_time_in_s = [7, 10, 4, 6]
def milli_second(x):
    return x * 1000
response_time_in_s = list(map(milli_second, response_time_in_s))
# response_time_in_s = list(map(lambda x: x * 1000, response_time_in_s)) -Lambda expression
print(response_time_in_s)

