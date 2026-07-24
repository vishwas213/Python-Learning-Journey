name = input("enter your name : ")
roll = input("enter your roll no : ")
marks = input("enter your marks : ")


with open("student.txt","a") as file:
    file.write(name + "," + roll + "," + marks + "\n")

print("student data saved ")
