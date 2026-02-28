# Nested Condition

y = 2000

# Check if the year is divisible by 4
if y % 4 == 0:

    # Check if the year is divisible by 100
    if y % 100 == 0:

        # Check if the year is divisible by 400
        if y % 400 == 0:

            # Divisible by 400, it is a leap year
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

# Single Condition

y = 1900

# Check if the year is a leap year using a single condition
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# Using Calendar Module

import calendar
y = 2000

# Use the built-in isleap function to check if the year is a leap year
if calendar.isleap(y):
    print("Leap year")
else:
    print("Not a leap year")

# Using Lambda function

y = 1900

# Lambda function to check if a year is a leap year
leap = lambda x: (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)

if leap(y):
    print("Leap year")
else:
    print("Not a leap year")

# Using decorators

def leap_year(input_year):
    if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
result = leap_year(year)
print(result)

