dic = {
    "name": "koushik",
    "age": 19,
    "country": "India"
}

# print(dic["name"])
# print(dic["name"])
# print(dic.get("name"))
# print(dic.keys())
# print(dic.values())

# for key in dic:
#     print(f"The value corresponding to {key} is {dic[key]}")

print(dic.items())

for key, value in dic.items():
    print(f"The value corresponding to {key} is {dic[key]}")
