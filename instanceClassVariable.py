class Employee:
    companyName = "Apple"
    noOfEmployees = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 1.04
        Employee.noOfEmployees += 1

    def showDetails(self):
        print(
            f"The name of the Employe is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")


emp = Employee("Koushik")
emp.raise_amount = 0.34
emp.companyName = "Apple India"  # this is an instance variable.if instance variable is present then it will be overriden by class variable but instance variable is not present then it will show the class variable
emp.showDetails()
# Employee.showDetails(emp)
emp1 = Employee("Rohan")
emp1.showDetails()
