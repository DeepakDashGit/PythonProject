# Palindrome of a string

string = input("Enter a string: ").lower()

if string == string[::-1]:   # [::-1] → reverses the string
    print("Palindrome")
else:
    print("Not a palindrome")


