score = int(input("Enter your score: "))
if 90 <= score <=100:
    print("Your grade is: A")
elif 70 <= score <=89:
    print("Your grade is: B")
elif 50 <= score <=69:
    print("Your grade is: C")
elif 30 <= score <=49:
    print("Your grade is: D")
elif 0 <= score <=29:
    print("Your grade is: F")
elif score <0:
    print("Invalid score! Please enter between 0 and 100.")
else:
    print("Invalid score! Please enter between 0 and 100.")
