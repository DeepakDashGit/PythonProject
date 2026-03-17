my_list = [35, 'b', False, 0.8, 'e']

my_list[1] = "Deepak"

for item in my_list:
    print(item)

# range() function returns a list
# append() append object to end of the list
my_list.append(4)
print(my_list)

# my_list.pop(3)
# print(my_list)

# del my_list[2]
# print(my_list)

my_list.extend(["j10", True, 5])
print(my_list)

my_list.remove(5)
print(my_list)

# my_list.reverse()
# print(my_list)

my_list.insert(1, "Inserted")
print(my_list)

my_list[2] = "DEEPAK"
print(my_list)

my_list2 =my_list.copy()
print(my_list)
print(my_list2)

my_list2.clear()
print(my_list2)

#Slicing
new_list = [2,4,5,7,9,15]
print(new_list[1:5]) # it will print [4,5,7,9]
print("apple" in new_list)
print(7 in new_list)
