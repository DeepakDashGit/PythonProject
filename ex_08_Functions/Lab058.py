#create a program to sum of three number from the user input
#if the user doesn't enter any number use default as 100, 200, 300

# nu1 = int(input("Enter first number: "))
# nu2 = int(input("Enter second number: "))
# nu3 = int(input("Enter third number: "))

def sum_of_three_number(nu1=100, nu2=200, nu3=300):
    return nu1 + nu2 + nu3

# result0 = sum_of_three_number(nu1, nu2, nu3)
# print(result0)

result1 = sum_of_three_number(10, 20, 30)
print(result1)

result2 = sum_of_three_number(nu1=25, nu2=25)
print(result2)

result3 = sum_of_three_number(nu1=25)
print(result3)

result4 = sum_of_three_number()
print(result4)

