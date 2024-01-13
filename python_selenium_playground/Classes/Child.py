from python_selenium_playground.Classes.Calculator import Calculator


class Child(Calculator):
    num2 = 200

    def __init__(self):
        super().__init__(69, 420)

    def get_complete_data(self):
        return self.num2 + self.num + self.sum_members()


obj = Child()
print(obj.get_complete_data())
