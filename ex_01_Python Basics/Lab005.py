num1 = int(input("first no: "))
num2 = int(input("second no: "))

#print(num1 // num2, num1 % num2)

#print(divmod(num1, num2))

if  num2 != 0:
    quotient, remainder = divmod(num1, num2)
    print("Quotient: ", quotient)
    print("Remainder: ", remainder)
else:
    print("Error: Number cannot be divided by ZERO!")
