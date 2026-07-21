students = []

while True:

    print("\n=====================")
    print(" Student Result System")
    print("=====================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        name = input("Enter Name: ")
        roll = int(input("Enter Roll Number: "))
        marks = int(input("Enter Marks: "))

        student = {
            "name": name,
            "roll": roll,
            "marks": marks
        }

        students.append(student)

        print("Student Added Successfully!")

    elif choice == 2:

        if len(students) == 0:
            print("No students found.")

        else:
            for student in students:
                print("-----------------")
                print("Name :", student["name"])
                print("Roll :", student["roll"])
                print("Marks:", student["marks"])

    elif choice == 3:

        search = input("Enter Name: ")

        found = False

        for student in students:
            if student["name"] == search:
                print("-----------------")
                print("Name :", student["name"])
                print("Roll :", student["roll"])
                print("Marks:", student["marks"])
                found = True
                break

        if found == False:
            print("Student Not Found")

    elif choice == 4:

        print("Thank You!")
        break

    else:
        print("Invalid Choice")
