class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def addition(self):
        print(self.a + self.b)

    def subtraction(self):
        print(self.a - self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

calc = Calculator(8, 4)
calc.addition()
calc.multiplication()