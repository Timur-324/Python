import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def length(self):
        return math.sqrt((self.p2.x - self.p1.x) ** 2 + 
                         (self.p2.y - self.p1.y) ** 2)
    def midpoint(self):
        mid_x = (self.p1.x + self.p2.x) / 2
        mid_y = (self.p1.y + self.p2.y) / 2
        return Point(mid_x, mid_y)
    
p1 = Point(0, 0)
p2 = Point(3, 4)

segment = Segment(p1, p2)

print(f"Отрезок: {p1} — {p2}")
print(f"Длина: {segment.length():.2f}")
print(f"Середина: {segment.midpoint()}")