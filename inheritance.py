# Inheritance : Below we have imported Calculator class from oops_demo.py file which is
# a parent class.

from oops_demo import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 5)

    def getCompleteData(self):
        return self.num2 + self.num + self.addition()  # we are able to access the variables of parent class here i.e. num


obj = ChildImpl()
print(obj.getCompleteData())
