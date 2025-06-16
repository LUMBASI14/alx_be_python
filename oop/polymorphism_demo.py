class Shape:
  def __init__(self):
    self.area = area

class Rectangle(Shape):
  def area(self, length, width):
    super().__init__(self)
    self.area = length * width
    return self.area
    
class Circle(Shape):
  import math
  def area(self, radius):
    super().__init__(self)
    self.area = math.pi * radius * radius
    return self.area
  
    
