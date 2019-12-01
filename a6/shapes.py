class Circle:

  PI = 3.1415

  def __init__(self, r):
    self.radius = r
 
  def area(self):
    return Circle.PI * self.radius * self.radius

  def circumference(self):
    return 2.0 * Circle.PI * self.radius

class Rectangle:
    
  def  __init__(self, l,b):
    self.length = l
    self.breadth = b

  def area(self):
    return self.length*self.breadth
  
  def circumference(self):
    return 2*(self.length+self.breadth)
