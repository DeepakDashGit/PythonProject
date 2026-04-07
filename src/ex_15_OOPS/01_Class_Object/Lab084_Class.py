class Student:

    # constructor
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age        # attribute

    # method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# object creation
# Student() - Object, Actual instance created
# s1 - Object Reference, Variable pointing to object
s1 = Student("Deepak", 25)

# accessing attributes
print(s1.name)
print(s1.age)

# calling method
s1.display()

# Real-Life Analogy

# Class → Car design
# Object → Your car
# Constructor → Sets value (color, model)
# Method → start(), stop()
# self → your specific car
# Attribute - color, model, speed, fuel
