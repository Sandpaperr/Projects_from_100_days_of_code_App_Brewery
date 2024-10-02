import os

FILE = os.path.join(os.getcwd(), "day 24 files", "my_file.txt")
with open(FILE) as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="w") as file:
    file.write("\nHello baby, I am here")