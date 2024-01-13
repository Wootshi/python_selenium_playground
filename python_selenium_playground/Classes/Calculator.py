class Calculator:
    num = 100  # class variable

    # constructor w/o parameters
    # def __init__(self):
    #     print("I am a constructor")

    # parametrized constructor.
    # Multiple constructors are not supported in Python, gotta work around it
    def __init__(self, a, b):
        self.ass = a
        self.bss = b
        print("I am a constructor with params")

    def get_data(self):
        print("Executing as a method in class")

    def sum_members(self):
        return self.ass + self.bss + self.num + Calculator.num
        # you can call upon Class variables (static ones) like that
        # contrary to java, you must not
        # declare class variables first in order to use them later
        # these are pulled right directly from constructor, where they are initiated


# 'new' operator is not required in Python.
obj = Calculator(2, 3)  # syntax to create an object in Python
obj.get_data()
print(obj.num)
print(obj.sum_members())

print("---------------")
obj1 = Calculator(4, 5)
obj1.get_data()
print(obj1.num)
print(obj1.sum_members())
