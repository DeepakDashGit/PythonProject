def print_multiple_args(*args):
    #*args is List
    for i in args:
        print(i)
    #print(*args)
print_multiple_args(1, 2, 3, 4, 5)
print_multiple_args("Deepak")
print_multiple_args("Deepak", "Ranjan", "Dash")
print_multiple_args("Sky", 143, 3.5, True)


