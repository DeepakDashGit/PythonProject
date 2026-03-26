# count vowels and consonant in a string

input_string = "Hello World"

vowels = "aeiou"

count_vowels = 0
count_consonants = 0

# vowel_list = []
# consonant_list = []

for char in input_string.lower():
    if char.isalpha():
        if char in vowels:
            count_vowels += 1
            #vowel_list.append(char)
        else:
            count_consonants += 1
            #consonant_list.append(char)

print("Vowels count:", count_vowels)
#print("Vowels list:", vowel_list)

print("Consonants count:", count_consonants)
#print("Consonants list:", consonant_list)

