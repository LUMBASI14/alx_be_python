class Shape:
  def __init__(self):
    self.area = area

class Rectangle(Shape):
  def area(self, length, width):
    super().__init__(self)
    self.length = length
    self.width = width
    self.area = self.length * self.width
    return self.area
    
class Circle(Shape):
  import math
  def area(self, radius):
    super().__init__(self)
    self.radius = radius
    self.area = math.pi * (radius ** 2)
    return self.area
  
    
