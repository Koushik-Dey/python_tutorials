# reading a file
# f = open("myfile.txt", "rb")
# # print(f)
# text = f.read()
# print(text)
# f.close()

# writing a file
# f = open("myfile.txt", "a")
# f.write("Hello World")
# f.close()

with open("myfile.txt", "a") as f:
    f.write("Hey i am inside with ")
