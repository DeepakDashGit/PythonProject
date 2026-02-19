# take user input and print quotient and reminder

num1 = float(input("Enter First Number- "))
num2 = float(input("Enter Second Number- "))

quotient = num1 // num2
reminder = num1 % num2

print(quotient)
print(reminder)

print(divmod(num1,num2))
print(num1 // num2, num1 % num2)

quotient, remainder = divmod(num1, num2)
print("Quotient: ", quotient, "remainder: ", remainder)

