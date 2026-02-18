#check weather the username or password is correct
#username = "admin"
#password = "1234"   print(login successful) print(invalid credential)

username = input("Enter username: ").strip()
password = input("Enter password: ").strip()
if username == "admin" and password == "1234":
    print("login Successful")
else:
    print("Invalid Credential")

# Leap year calculation

Leap_Year = int(input("Enter Year: "))
if (Leap_Year % 400 == 0) or(Leap_Year % 4 == 0 and Leap_Year % 100 != 0) :
    print(f"{Leap_Year} is a leap year")
else:
    print(f"{Leap_Year} is not a leap year")