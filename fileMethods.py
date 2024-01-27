# f = open("myfile.txt", "r")
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"marks of student {i} in maths is : {m1}")
#     print(f"marks of student {i} in English is : {m2}")
#     print(f"marks of student {i} in SST is : {m3}")
#     print(line)

# f = open('myfile3.txt', "w")
# lines = ["line 1\n", "line 2\n", "line 3\n"]
# f.writelines(lines)
# f.close()

# num = 7

# for i in range(2, num):
#     if num % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

# with open("file.txt", "a")as file:
#     file.write("\nHe will be a good programmer")

# with open("file.txt", "r") as file:
#     text = file.read()
#     print(text)

# numOne = int(input("Enter first number: "))
# numTwo = int(input("Enter second number: "))

# operator = input("which operation you want to do (+,-,*,/): ")

# if operator == "+":
#     print(numOne + numTwo)
# elif operator == "-":
#     print(numOne-numTwo)
# elif operator == "*":
#     print(numOne * numTwo)
# elif operator == "/":
#     print(numOne / numTwo)
# else:
#     print("Something went wrong")


# primeInput = int(input("Enter Your number: "))

# for i in range(2, primeInput):
#     if primeInput % i == 0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)


# print(factorial(5))

# <------------------smallest number------------->

# numOne = int(input("Enter your frist number : "))
# numTwo = int(input("Enter your second number : "))
# numThree = int(input("Enter your third number : "))

# if numOne < numTwo and numOne < numThree:
#     print(f"{numOne} is the smallest number")
# elif numTwo < numOne and numTwo < numThree:
#     print(f"{numTwo} is the smallest number")
# elif numThree < numOne and numThree < numTwo:
#     print(f"{numThree} is the smallest number")

# <------------------------end-------------------->

# <---------------octal to decimal---------------->

# num = input("Enter your octal number: ")
# decimal = int(num, 8)

# print(f"Decimal value of {num} is {decimal}")

# <--------------------end------------------------>

# <--------------find the even numbers from a list------->

# myList = [1, 2, 3, 4, 6, 8, 10, 22, 44, 66, 86, 24]


# def findEvenNumber(givenList):
#     for i in givenList:
#         if i % 2 == 0:
#             print(i)


# findEvenNumber(myList)


# with open("koushik.txt", "w") as file:
#     file.write("Hey my name is koushik")

with open("koushik.txt", "r")as file:
    text = file.read()
    print(text)
