countries = ("Spain", "Italy", "India", "England", "Italy",
             "Germarny", "Spain", "Spain")  # tupples are immutable

# print("count of tupple: ", tuple.count(countries, "Spain"))

print("index of Indian : ", countries.index("India"))
print("index of Indian : ", countries.index("India", 0, 3))
print(len(countries))

# temp = list(countries)
# temp.append("Russia")
# print(temp)

# print(countries.index("Spain", 3, 7))
