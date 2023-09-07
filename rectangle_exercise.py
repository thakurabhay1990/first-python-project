# Program to find the area and circumference of Rectangle

class Rectangle:
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth

    def area_of_rectangle(self):
        return self.l * self.b

    def circum_of_rectangle(self):
        return (2 * self.l) + (2 * self.b)


rect1 = Rectangle(2,4)
print(f"Area of Rectangle is {rect1.area_of_rectangle()}")
print(f"Circumference of Rectangle is {rect1.circum_of_rectangle()}")
