class Math:
    def __init__(self, num):
        self.num = num

    def addToNum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b


# result = Math.add(1, 2)
# print(result)  # Output: 3

a = Math(5)
a.addToNum(10)
print(a.num)
print(Math.add(7, 2))
