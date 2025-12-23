import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def distance_to_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
p1 = Point(3, 4)
p2 = Point(-2, 5)
dx, dy = 2, -3

print(f"Точка p1: ({p1.x}, {p1.y})")
print(f"Сдвиг на ({dx}, {dy})...")
p1.move(dx, dy)
print(f"p1 теперь: ({p1.x}, {p1.y})")
print(f"Расстояние p1 до (0,0): {p1.distance_to_origin():.2f}")

print("\n")
print(f"Точка p2: ({p2.x}, {p2.y})")
print(f"Расстояние p2 до (0,0): {p2.distance_to_origin():.2f}")