from functools import reduce

# MAP
# def cube(x):
#     return x*x*x


# l = [1, 2, 3, 4, 5]

# newL = map(lambda x: x*x*x, l)

# print(list(newL))

# FILTER


# def filter_function(a):
#     return a > 2


# filNewL = filter(filter_function, l)

# print(list(filNewL))


numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using reduce function

sum = reduce(lambda x, y: x+y, numbers)
print(sum)
