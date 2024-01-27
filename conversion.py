from datetime import date, timedelta

# octal to decimal

# octal = input("Enter your number: ")
# decimal = int(octal, 8)

# print(f"Decimal value of {octal} is {decimal}")


# decimal to octal
# decimal = int(input("Enter your number: "))
# octal = oct(decimal)

# print(f"octal value is {octal}")

# hexadecimal to decimal
# hexadecimal = input("Enter your hexadecimal number: ")
# decimal = int(hexadecimal, 16)

# print(f"decimal value of {hexadecimal} is {decimal}")

# decimal to hexadecimal
# decimal = int(input("Enter your number: "))
# hexadecimal = hex(decimal)

# print(f"hexadecimal value of {decimal} is {hexadecimal}")

# hexadecimal to octal
# hexadecimal = input("Enter your hexadecimal number: ")
# octal = int(oct(int(hexadecimal, 16))[2:])

# print(f"octal value of {hexadecimal} is {octal}")


# substract 5 days from current date

# days = input("Enter days to substract: ")
# dt = date.today() - timedelta(5)

# print(f"current date is {date.today()}")
# print(f"5 days ago the date was {dt}")

# python function that takes a list and return a new list with distinct elements from the first list
# myList = [1, 2, 2, 3, 3, 4, 4, 5, 6]
# disticntItems = set(myList)
# returnedList = list(disticntItems)
# print(returnedList)

# remove spaces from the keys in dictionary

dictOne = {
    "key 1": "valueOne",
    "key 2": "valueTwo",
    "key 3": "valueThree",
}

newDict = {}

for key, value in dictOne.items():
    new_key = key.replace(" ", "")
    newDict[new_key] = value

print(newDict)
