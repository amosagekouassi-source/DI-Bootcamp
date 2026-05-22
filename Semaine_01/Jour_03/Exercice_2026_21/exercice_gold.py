class circle():

  def __init__(self, radius=1.0):
    self.radius = radius

  def perimeter(self):
    return 2 * 3.14 * self.radius

  def area(self):
    return 3.14 * self.radius**2

# Create an instance of the circle class to access its methods and attributes
my_circle = circle(5.0) # Example with radius 5.0

print(f"Un cercle est un figure géométrique dont le périmètre est p= {my_circle.perimeter()} et dont l'aire = {my_circle.area()}.")