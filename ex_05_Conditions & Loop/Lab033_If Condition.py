"""
age = int(input("Enter age: "))
if age >= 21:
    print("Yes, you are allowed")
else:
    print("No, you are not allowed")
"""

while True:
    age_input = input("Enter age: ").strip()

    if age_input == "":
        print("Input cannot be empty.")
        continue

    try:
        age = float(age_input)

        if age < 0:
            print("Age cannot be negative.")
        elif age > 120:
            print("Invalid age. Enter a realistic value.")
        elif age >= 21:
            print("Yes, you are allowed.")
        else:
            print("No, you are not allowed.")
        break

    except ValueError:
        print("Invalid input. Only numeric values are allowed.")