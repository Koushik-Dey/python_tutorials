from typing import Any


class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f"The name of the employee is {self.name} str"

    def __repr__(self):
        return f"Employee({self.name})"

    def __call__(self):
        print("Hey i am called")


# e = Employee()
# print(e.name)
# print(len(e))
