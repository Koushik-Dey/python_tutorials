# s1 = {1, 2, 3, 5, 6}
# s2 = {4, 6, 7}
# print(s1.union(s2))
# print(s1, s2)
# s1.update(s2)
# print(s1, s2)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.intersection_update(cities2)
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2)
# print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
# print(cities.issuperset(cities2))
cities3 = {"Tokyo", "Madrid", "delhi"}
# print(cities.issuperset(cities3))
# print(cities3.issubset(cities))


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
# print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
# print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Tokyo2")
# print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
# print(cities)
# print(item)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)
