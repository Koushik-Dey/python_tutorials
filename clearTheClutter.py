import os

files = os.listdir("images")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"images/{file}", f"images/{i}.png")
        i += 1
