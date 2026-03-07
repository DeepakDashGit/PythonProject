# *
# **
# ***

n = 5
for i in range(1,n+1):
    print("*" * i)

# Inverted right triangle (decreasing stars)
n = 5
for i in range(n, 0, -1):
    print("*" * i)

# Full pyramid
n = 5
for i in range(1, n+1):
    spaces = " " * (n - i)
    stars = "*" * (2*i - 1)
    print(spaces + stars)

# Inverted full pyramid
n = 5
for i in range(n, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2*i - 1)
    print(spaces + stars)

# Hollow pyramid
n = 5
for i in range(1, n+1):
    for j in range(1, 2*n):
        if j == n-i+1 or j == n+i-1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Diamond pattern
n = 5

for i in range(1, n+1):  # Upper pyramid
    spaces = " " * (n - i)
    stars = "*" * (2*i - 1)
    print(spaces + stars)

for i in range(n-1, 0, -1):  # Lower inverted pyramid
    spaces = " " * (n - i)
    stars = "*" * (2*i - 1)
    print(spaces + stars)

# Left-aligned pyramid
n = 5
for i in range(1, n+1):
    stars = "*" * i
    print(stars.ljust(n))

# Number pyramid
n = 5
for i in range(1, n+1):
    spaces = " " * (n - i)
    numbers = ""
    for j in range(1, i+1):
        numbers += str(j) + " "
    print(spaces + numbers)


