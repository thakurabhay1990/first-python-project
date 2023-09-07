# Program to find the Area and Circumference of the Circle
class Circle:
    pi = 3.14  # Class Object attribute

    def __init__(self, radius=10):
        self.radius = radius

    # Circumference = 2*pie*r
    def circumference(self):
        # circum = 2 * self.pi * self.radius
        # For accessing class object attribute we can also use "Classname.attribute"
        circum = 2 * Circle.pi * self.radius
        return circum

circle_1 = Circle()
print(circle_1.circumference())

circle_2= Circle(20)
print(circle_2.circumference())
