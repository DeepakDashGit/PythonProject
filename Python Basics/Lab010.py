# Leap_Year = int(input("Enter Year: "))
# if (Leap_Year % 400 == 0) or(Leap_Year % 4 == 0 and Leap_Year % 100 != 0) :
#     print(f"{Leap_Year} is a leap year")
# else:
#     print(f"{Leap_Year} is not a leap year")

# for i in range(1,10):
#     if i == 5:
#         print("five")
#     else:
#         print(i)

# for i in range(1,10):
#     print(i)
#     if i == 5:
#         break

# for i in range(1, 10):
# 	if i == 6:
# 		print(i)
# 	else:
# 		print("No Output")

# for i in range(1, 10):
# 	if i == 6 or i == 5:
# 		print(i)
# 	else:
# 		pass

for i in range(10):
	if i%2 == 0:
		continue
	else:
		print(i)
