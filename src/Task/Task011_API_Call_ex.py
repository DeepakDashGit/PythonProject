#Write a program to retry the API call 3 times until the response code becomes 200.
#If it still fails after 3 tries, print a failure message.

attempt = 1
max_attempt = 3
response = None
while attempt <= max_attempt:
    response = int(input("Enter response"))
    if response == 200:
        print("Test Passed")
        break
    else:
        print("Retrying...")
        attempt += 1
if response != 200:
    print("Test Failed after 3 attempts")

