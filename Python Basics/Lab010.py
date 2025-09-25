Leap_Year = int(input("Enter Year: "))
if (Leap_Year % 400 == 0) or(Leap_Year % 4 == 0 and Leap_Year % 100 != 0) :
    print(f"{Leap_Year} is a leap year")
else:
    print(f"{Leap_Year} is not a leap year")