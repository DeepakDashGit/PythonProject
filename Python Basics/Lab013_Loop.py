# N=1
# while N <= 10:
#     print(N)
#     N += 1

# n = 5
# for i in range(1, n + 1):
#     print(" *" * i)

# n = 5
# for i in range(1,n):
#     s = " " * (n-i)
#     st = "* " * i
#     print(s + st)

# n = 4
# for i in range(1,n):
#     s = " " * (n-i)
#     st = "*" * (i * 2 - 1)
#     print(s + st)

n = 4
for i in range(0,n):
    s = " " * (n-(i+1))
    st = "*" * ((i * 2) + 1)
    print(s + st)