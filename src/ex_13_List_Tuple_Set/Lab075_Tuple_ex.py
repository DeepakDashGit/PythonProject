# conversion of tuple to list

ex_tuple = ("linkedin.com", "facebook.com", "twitter.com")
print(ex_tuple)
conv_list = list(ex_tuple)
print(conv_list)

# conversion of list to tuple
conv_tuple = tuple(conv_list)
print(conv_tuple)

hero1 = ("Iron Man", "Hulk", "Thor", "Vision")
hero2 = ("Captain", "Ant Man", "Black Widow", "Falcon")
avengers = (hero1, hero2)
print(hero1)
print(hero2)
print(avengers)
print(avengers[0])
print(avengers[0][0])

city = ("Cuttack", "Baleswar", "Bhubaneswar")
print("Cuttack" in city)
print(len(city))

for c in city:
    print(c)

num5 = "Deepak" * 3
print(num5)

num6 = (1, 2, 3) * 3
print(num6)