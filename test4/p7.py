import math
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return math.pi*(self.r**2)
    def perimeter(self):
        return 2* math.pi* self.r
r_input=int(input())
circle=Circle(r_input)

print("area", circle.area())
print("perimeter",circle.perimeter())