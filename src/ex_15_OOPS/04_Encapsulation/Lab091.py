from dotenv import load_dotenv
import os
load_dotenv(override=True)

print(f"Loaded Username: {os.getenv('username','')}")
print(f"Loaded Password: {os.getenv('password', '')}")

class LoginWeb:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if self.username == os.getenv("username") and self.password == os.getenv("PASSWORD"):
            print('Login Successful')
        else:
            print('Login Failed')

email = input('Enter your email: ').strip()
key = input('Enter your password: ').strip()

site = LoginWeb(email, key)
site.login()

