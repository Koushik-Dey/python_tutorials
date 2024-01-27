marks = [3, 4, 5, "Koushik", True, 2, 8, 9]  # list are mutable

# print(marks[-3])


# same things apply for strings
# if "shik" in "Koushik":
#     print("Yes")
# else:
#     print("No")

# print(marks)
# print(marks[1:])
# print(marks[1:-1])
# print(marks[1:8:2])

lst = [i*i for i in range(4)]

print(lst)
lst = [i*i for i in range(10) if i % 2 == 0]

print(lst)
