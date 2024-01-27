tup = (1, 5, 6, "green", True, 342, 76)  # tuppels are immutable
print(type(tup))
print(len(tup))
print(tup[3])
print(tup[-1])

if 342 in tup:
    print("Yes this is present in tup")

tup2 = tup[1:4]
print(tup2)

# slice tupples will return new tupple
