# Even numbers
nums = [1, 2, 3, 4, 5]
def even_numb(num):
    return num % 2 == 0

print_even_numbers = list(filter(even_numb, nums))
print(print_even_numbers)

# Test result
test_result = ["pass", "Fail", "Pass", "Skip", "Fail"]
def pass_result(value):
    return value in ["pass", "Pass", "PASS"]
print_pass_result = list(filter(pass_result, test_result))
print(print_pass_result)

# Empty string

strings = ["a", "b", "" , "c", "d", "", "e"]

def remove_empty(x):
    return x != ""

new_strings = list(filter(remove_empty, strings))
print(new_strings)

# new_string2 = list(filter(None, strings))
# print(new_string2)


