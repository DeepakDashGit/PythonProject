# Find the non-repeating character in a string using Set


#print("swiss".count("s"))

def check_char(text):
    for char in text:
       if text.count(char) == 1:
            return char
    return None
res = check_char("require")
print(f"First non repeating character is: {res}")


