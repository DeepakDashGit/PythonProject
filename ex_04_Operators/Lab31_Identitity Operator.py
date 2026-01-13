list_a = [1, 2, 3]
list_b = [1, 2, 3]  # A new list with the same values
list_c = list_a      # list_c now refers to the same object as list_a

# Compare list_a and list_b
print(list_a is list_b)

# Compare list_a and list_c
print(list_a is list_c)


print(list_a is not list_b)