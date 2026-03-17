key = ['name', 'Role', 'Experience']
value = ['Robot', 'Sales', '4']

my_dict = dict(zip(key, value))
print(my_dict)

# Merge two dictionary

dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'d':1, 'e':2, 'f':3}

merge_dict = dict1 | dict2
print(merge_dict)

