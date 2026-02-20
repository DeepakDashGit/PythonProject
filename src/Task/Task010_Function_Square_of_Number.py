# Q - Create a function which will take a positive number from the
# user and perform square of the number?

def square_number():
    try:
        num = int(input("Enter a positive number: "))
        if num > 0:
            print("Square is:", num * num)
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input.")




