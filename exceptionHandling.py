# a = input("Enter the number: ")
# print(f"multiplication table of {a} is: ")

# try:
#     for i in range(1, 11):
#         print(f"{int(a)} x {i} = {int(a) * i}")
# except Exception as e:
#     print(f"Reason for exception: {e}")

# print("some lines of code")
# print("End of program")

try:
    num = int(input("Enter a number: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error: Index out of bounds")
