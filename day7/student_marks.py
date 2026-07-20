name = (input("enter your name : "))
marks = int(input("enter your marks: "))
student={
    "Name" : name,
    "Marks": marks,
}

for key,value in student.items():
    print(key,":",value)