firstNum = input("Enter your first number")
secondNum = input("Enter your first number")
chooseOperator = input("Enter which operation you want")

if chooseOperator == "+":
    print(int(firstNum) + int(secondNum))
elif chooseOperator == "-":
    print(int(firstNum) - int(secondNum))
elif chooseOperator == "*":
    print(int(firstNum) * int(secondNum))
elif chooseOperator == "/":
    print(int(firstNum) / int(secondNum))
else:
    print("Please enter a valid number")
