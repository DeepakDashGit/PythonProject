# Lists are used to store multiple items in a single variable.
# Lists are ordered, mutable and allow duplicates, suitable for dynamic data.
# parenthesis - []

my_list1 = [1, 2, 3]
my_list2 = [4, "Deepak", 0.2, True]

print(my_list1)
print(type(my_list2))
print(len(my_list2))

print(my_list2[0])
#print(my_list2[5]) # list index out of range

# list creation and comprehension
l = list(range(1,5))
print(l)
print(l[3])

# Nested lists
multi_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(multi_list[1])