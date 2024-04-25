class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def perimeter(self):
        print(2 * (self.x + self.y))
    
    def square(self):
        print(self.x * self.y)

rectangle = Rectangle(2, 3)
rectangle.perimeter()
rectangle.square()