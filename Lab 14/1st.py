import math  
class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


r = float(input("Enter radius of circle: ")) 
c = Circle(r) 

print("Area of circle:", c.area())
print("Perimeter of circle:", c.perimeter())



