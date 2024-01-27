a = "Koushik"

# strings are immutable
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Koushik", "Harry"))
print(a.split(" "))

blogHeading = "introduction to js"
print(blogHeading.capitalize())

str1 = "Welcome to the Console"
print(len(str1))
print(len(str1.center(50)))

print(a.count("Koushik"))

print(str1.endswith("Console"))

str2 = "He's name is Dan. He is an honest man"

print(str2.find("is"))

# print(str1.index("is"))

str3 = "WelcomeTOTheConsole"
print(str3.isalnum())

str4 = "Welcome00"
print(str4.isalpha())
