class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


square = Square(5)
print(f"Square {square.width}x{square.height}:")
print(f" Площадь: {square.area()}")
print(f" Периметр: {square.perimeter()}")