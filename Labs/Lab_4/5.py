import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def __str__(self):
        if self.width == self.height:
            return f"Square {self.width}x{self.height}:"
        else:
            return f"Rectangle {self.width}x{self.height}:"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return round(math.pi * self.radius ** 2, 2)
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)
    def __str__(self):
        return f"Circle R={self.radius}:"
    
shapes = [Rectangle(5, 5), Circle(5)]

for shape in shapes:
    print(shape)
    print(f"Площадь: {shape.area():.2f}")
    print(f"Периметр: {shape.perimeter():.2f}\n")