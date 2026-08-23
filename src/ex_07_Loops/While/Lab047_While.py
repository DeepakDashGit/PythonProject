i = 0  #Initialization
while i < 10:  #Condition
    print(i)
    i = i+1   #Updation

count = 0
while count < 5:
    print(count)
    count += 1
    

N = 10    # It will give the result of sum of 10 to 1 (10+9+8+7+6+5+4+3+2+1)
s = 0

while True:
    s += N
    N -= 1

    if N == 0:
        break

print(s)