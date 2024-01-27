class Person:
    def __init__(self, name, occ):
        print("Hey i am a person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Koushik", "Engineer")
b = Person("Divya", "HR")
c = Person(1, 2)

a.info()
b.info()
