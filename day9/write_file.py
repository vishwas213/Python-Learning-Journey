name = input("enter your names : ")
with open("name.txt", "w") as file:
    file.write(name)
