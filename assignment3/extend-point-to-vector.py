# Task 5: Extending a Class
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx**2 + dy**2)

class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

# Testing Point methods
p1 = Point(0, 0)
p2 = Point(3, 4)
p3 = Point(0, 0)

print(p1)
print(p1 == p2)
print(p1 == p3)
print(p1.distance(p2))

# Testing Vector methods
v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2

print(v3)