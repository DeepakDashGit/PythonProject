'''
# Leap year

Leap_Year = int(input("Enter Year: "))
if (Leap_Year % 400 == 0) or(Leap_Year % 4 == 0 and Leap_Year % 100 != 0) :
    print(f"{Leap_Year} is a leap year")
else:
    print(f"{Leap_Year} is not a leap year")
'''

# write a program that prints numbers from 1 to 100. However, for multiples of 3, print "Fizz"
#insted of number and for multiples of 5, print "Buzz". For numbers which are multiples of 3 and 5
#print "FizzBuzz".

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)







