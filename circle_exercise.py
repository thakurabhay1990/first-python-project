# Program to find the Area and Circumference of the Circle
class Circle:
    pi = 3.14  # Class Object attribute

    def __init__(self, radius=10):
        self.radius = radius
        self.area= Circle.pi * radius * radius

    # Circumference = 2*pie*r
    def circumference(self):
        # circum = 2 * self.pi * self.radius
        # For accessing class object attribute we can also use "Classname.attribute"
        circum = 2 * Circle.pi * self.radius
        return circum

circle_1 = Circle()
print(f"The circumference of the circle is: {circle_1.circumference()}")
print(f"The area of circle is : {circle_1.area}")

circle_2= Circle(20)
print(f"The circumference of the circle is: {circle_2.circumference()}")
