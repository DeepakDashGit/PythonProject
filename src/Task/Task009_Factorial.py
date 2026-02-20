num = int(input("Enter a number to know the factorial: "))

fact = 1

if num < 0:
    print("Factorial is not defined")
elif num == 0:
    print("Factorial = ", fact)
else:
    for i in range(1, num+1):
        fact *= i
print("Factorial is", fact)

