# Sets are used to store multiple items in a single variable
# Sets are unordered, mutable and can contain duplicate
# parenthesis - {}

list1 = {1, 2, 3, 5, 3, 2}
print(list1)

list2 = (10, True, 2.5, True, "Hello", 10, 1) # if we keep 1 and true in a list it will print 1 or true not both
set1 = set(list2)
print(set1)

list3 = ["Best", False, 33.34, 57, False, "Best", 57]
set2 = set(list3)
print(set2)

empty_set = set()
print(empty_set)  # it will create empty set. sme as list and tuple

for item in list2:
    print(item)

