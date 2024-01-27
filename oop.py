# RailwayForm ---> Class [blueprint]
# koushik --> form of koushik with his ifno --> Object [entity]
# Rahul --> form of rahul with his info --> Object [entity]
# Abir --> form of abir with his info --> Object [entity]

class Person:
    name = "Koushik"
    occupation = "Engineer"
    netWorth = 10

    def info(self):
        # self is a refference to the current instance of the object
        print(f"{self.name} is a {self.occupation}")


a = Person()
print(a.occupation)
a.info()
