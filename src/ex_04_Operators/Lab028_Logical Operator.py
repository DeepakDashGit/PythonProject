a, b = 5, 10
print(a > 0 and b > 0 )
print(a > 0 or b < 0)
print(not(a > 0))  # not operator is used to reverse the logical result value. Here it will show False.

f = False
t = True
print(f or t)
print(f and t)

username = ""  # Empty string is Falsy

if not username:
    print("Error: Username cannot be blank!")