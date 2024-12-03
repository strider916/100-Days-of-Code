with open("my_file.txt", mode="r") as file:
    content = file.read()
    print(content)

with open("my_file.txt", mode="a") as file:
    file.write("\nHello, new world!")

with open("my_file.txt", mode="r") as file:
    content = file.read()
    print(content)
