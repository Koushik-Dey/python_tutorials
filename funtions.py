# def calculateGmean(a, b):
#     mean = (a*b)/(a+b)
#     print(mean)


# def isGreater(a, b):
#     if (a > b):
#         print('First number is greater')
#     else:
#         print("second number is greater")


# def isLesser(a, b):
#     pass


# a = 9
# b = 8
# isGreater(a, b)
# calculateGmean(a, b)
# c = 8
# d = 7
# isGreater(c, d)
# calculateGmean(c, d)


# def average(a, b, c=1):
#     print("The average is ", (a + b + c)/2)


# average(4, 11)
# average(12, 5)


# def name(fname, mname="Jhon", lname="watson"):
#     print("Hello", fname, mname, lname)


# name("Koushik", "Chandra", "wilson")


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)


print(average(5, 6, 7, 1))


def name(**name):
    print(name)
    print("Hello ,", name["fname"], name["mname"], name["lname"])
