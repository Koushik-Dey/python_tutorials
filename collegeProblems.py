# Write a Python function that takes a list and returns a new list with distinct elements from the first list.

sample_list = [1, 2, 3, 4, 2, 2, 3, 3, 5, 5, 6]


def distinct_list(lst):
    print(list(set(lst)))


# distinct_list(sample_list)

# Write a Python program to print the even numbers from a given list.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for num in lst:
#     if num % 2 == 0:
#         print(f"{num} is even number")


# Write a Python function to check whether a number falls within a given range.

num = int(input("Enter a number between 1 to 10: "))


def fallsNumber(num):
    if num in range(1, 10):
        print(f"{num} is between 1 to 10")


fallsNumber(num)
