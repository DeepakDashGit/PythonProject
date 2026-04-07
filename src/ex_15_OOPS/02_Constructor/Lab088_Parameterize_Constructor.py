class Calc:
    a = None
    b = None
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

result = Calc(4,3)
print(f"Sum of the numbers:{result.sum()}")
print(f"Sub of the numbers:{result.sub()}")
print(f"Multiplication of the numbers:{result.mul()}")
print(f"Division of the numbers:{result.div()}")

