# Ex-1

find_even_odd = lambda num: num % 2 == 0
print(find_even_odd(int(input("Enter a number: "))))

# Ex-2

user_input = int(input("Enter a number: "))
check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
#result = check_even_odd(user_input)
#print(result)
print(check_even_odd(user_input))

# Ex-3

import math
print((lambda : math.pow((int(input("Enter a number:"))),2,))())




