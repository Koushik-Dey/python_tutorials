letter = "Hey my name is {0} and I am form {1}"
country = "India"
name = 'Koushik'

print(letter.format(name, country))
print(
    f"We use f-stirng like this Hey my name is {name} and I am form {country}")

# if we want show variable as it is we use {{}}- this syntax
print(
    f"We use f-stirng like this Hey my name is {{name}} and I am form {country}")

txt = "For only {price:.2f} dollars!"

print(txt.format(price=49.098))

print(type(f"{2* 30}"))
