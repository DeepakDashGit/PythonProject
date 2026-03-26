#remove duplicate values
my_dict = {'a':10, 'b':20, 'c':30, 'd':10}

unique_value = set()
result = {}

for key, value in my_dict.items():
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)
print(result)
