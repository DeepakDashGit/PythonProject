# A static method in Python is a method that belongs to a class
# rather than an instance of the class. This means it can be
# called directly on the class itself, without the need to create an instance of the class.

class Calc:
    def __init__(self):
        print("CL")

    @staticmethod
    def sum(a,b):
        return a + b
    @staticmethod
    def sub(a,b):
        return a - b
    @staticmethod
    def multi(a,b):
        return a * b
    @staticmethod
    def divide(a,b):
        return a / b
    @staticmethod
    def pow(a,b):
        return a ** b
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

#compute = Calc()
print(f"Sum of the number:{Calc.sum(x,y)}")
print(f"Sub of the number:{Calc.sub(x,y)}")
# print(f"Multiplication of the number:{compute.multi(x,y)}")
# print(f"Division of the number:{compute.divide(x,y)}")
# print(f"Power of the number:{compute.pow(x,y)}")


