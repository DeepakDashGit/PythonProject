Leap_Year = int(input("Enter Year: "))
if (Leap_Year % 400 == 0) or(Leap_Year % 4 == 0 and Leap_Year % 100 != 0) :
    print(f"{Leap_Year} is a leap year")
else:
    print(f"{Leap_Year} is not a leap year")

# S1 = int(input("Enter S1: "))
# S2 = int(input("Enter S2: "))
# S3 = int(input("Enter S3: "))
# if S1 == S2 == S3:
#     print("It is a equilateral triangle")
# elif S1 == S2 or S2 == S3 or S3 == S1:
#     print("It is a isosceles triangle")
# else:
#     print("It is a scalene triangle")
