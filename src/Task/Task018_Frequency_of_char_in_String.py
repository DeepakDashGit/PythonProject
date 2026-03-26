# frequency of a character in a string
# write a program to count each character present in a string

string = input("Enter a string: ")

char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
