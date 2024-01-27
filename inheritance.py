class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"THe name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


e = Employee("Rohan Das", 400)
e.showDetails()
e2 = Programmer("Koushik", 4100)
e2.showDetails()
e2.showLanguage()
