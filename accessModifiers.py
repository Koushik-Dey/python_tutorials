# Public access modifier
# Private access modifier
# Protected access modifier

# class Employee:
#     def __init__(self):
#         self.__name = "Koushik"


# a = Employee()
# # print(a.name) can not be accessed directly
# print(a._Employee__name)  # can be accessed indirectly


class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"


class Subject(Student):  # inherited class
    pass


obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())
