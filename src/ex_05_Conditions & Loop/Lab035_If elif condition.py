num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if num1 < 0 or num2 < 0:
    print("Enter a positive number")
elif num1 > num2:
    print("Maximum", num1)
elif num1 == num2:
    print("Both are equal")

else:
    print("Minimum",num2)

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a >= b and a >= c:
    print(a, " is greater")
elif b >= a and b >= c:
    print(b, "is greater")
else:
    print(c, "is greater")
