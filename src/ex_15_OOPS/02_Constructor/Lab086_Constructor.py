class Person:
    def __init__(self):
        self.name = input("Please enter your name: ")
        self.age = input("Please enter your age: ")
        self.phone = input("Please enter your phone number: ")
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Phone:", self.phone)

details = Person()
details.display()

