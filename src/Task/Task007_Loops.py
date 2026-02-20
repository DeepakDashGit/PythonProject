#check weather the username or password is correct
#username = "admin"
#password = "1234"   print(login successful) print(invalid credential)

username = input("Enter username: ").strip()
password = input("Enter password: ").strip()
if username == "admin" and password == "1234":
    print("login Successful")
else:
    print("Invalid Credential")

