# Classes : They are the user defined blueprint or prototype
# methods, class variables, instance variable, constructors etc.
# There are 2 types of variables : class variables & instance variables
# Self keyword is mandatory for calling variable names into method
# New keyword is not required when you create object


class Calculator:
    num = 100 # Class variables (it will remain constant)

# Constructor : It is one of the method which is automatically called when we created object for any class
# Also, the constructor name should be __init__
# NOTE : if there is no constructor created then default constructor will be called.
    # default constructor
    def __init__(self, a, b):
        self.firstNumber = a # this is an instance variable
        self.secondNumber = b # this is an instance variable
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as a method in a class")

    def addition(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3) # syntax to create objects in python for a class
obj.getData()
print(obj.num)
print(obj.addition())

obj1 = Calculator(4, 5) # syntax to create objects in python for a class
obj1.getData()
print(obj1.num)
print(obj1.addition())
