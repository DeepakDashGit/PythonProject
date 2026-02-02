
try:
    grade = float(input("Enter the grade: ").strip())

    if 90 <= grade <= 100:
        print("You got grade A")
    elif 80 <= grade <= 89:
        print("You got grade B")
    elif 70 <= grade <= 79:
        print("You got grade C")
    elif 60 <= grade <= 69:
        print("You got grade D")
    elif 0 <= grade <= 59:
        print("You got grade F")
    else:
        print("Enter correct number")
except ValueError:
    print("Invalid input. Only numeric values are allowed.")


"""
try:
    grade = float(input("Enter the grade: ").strip())

    if grade < 0 or grade > 100:
        print("Grade must be between 0 and 100")

    elif grade >= 90:
        print("You got grade A")

    elif grade >= 80:
        print("You got grade B")

    elif grade >= 70:
        print("You got grade C")

    elif grade >= 60:
        print("You got grade D")

    else:
        print("You got grade F")

except ValueError:
    print("Invalid input. Only numeric values are allowed.")
"""
