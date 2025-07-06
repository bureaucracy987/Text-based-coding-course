import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        
        return math.pi * self.radius ** 2

    def perimeter(self):
        
        return 2 * math.pi * self.radius


circle1 = Circle(56)


print("Radius:", circle1.radius)
print("Area:", round(circle1.area(), 2))
print("Perimeter (Circumference):", round(circle1.perimeter(), 2))

        

