my_dict = {
    'Name': 'Deepak',
    'Age' : '34',
    'City': 'Cuttack',
    'Role': 'QA',
    'Exp' : '3.8'
}

print(my_dict)
print(my_dict['Name'])
print(my_dict['Age'])

my_dict['Role'] = 'Manual QA'
print(my_dict)

print('Age' in my_dict)
print('Title' in my_dict)

del my_dict['Age']
print(my_dict)

for key, value in my_dict.items():
    print(key, value)


