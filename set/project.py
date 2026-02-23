"""Create a simple Student Record Management System in Python that runs in the Command Prompt (CMD) and uses tuples to store student information. Each student should be stored as a tuple containing Student ID, Student Name, Course Name, and Marks. The program should display a menu that allows the user to add a new student record, view all student records, search for a student by Student ID, update an existing student’s details, and remove a student from the system. Since tuples are immutable, when updating a student record, the old tuple should be replaced with a new tuple containing the updated information. The program should continue running until the user chooses the exit option, and it should use only basic Python concepts such as input, print, tuples, loops, and conditional statements without using classes, files, or external libraries."""


# Student Record Management System using SET and TUPLES

students = set()

while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    # Add Student
    if choice == "1":
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        marks = input("Enter Marks: ")

        student = (sid, name, course, marks)
        students.add(student)

        print("Student added!")

    # View Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for s in students:
                print("ID:", s[0], "| Name:", s[1], "| Course:", s[2], "| Marks:", s[3])

    # Search Student
    elif choice == "3":
        sid = input("Enter ID to search: ")
        found = False

        for s in students:
            if s[0] == sid:
                print("Found:", s)
                found = True
                break

        if not found:
            print("Student not found.")

    # Update Student
    elif choice == "4":
        sid = input("Enter ID to update: ")
        found = False

        for s in students:
            if s[0] == sid:
                students.remove(s)

                name = input("Enter new Name: ")
                course = input("Enter new Course: ")
                marks = input("Enter new Marks: ")

                new_student = (sid, name, course, marks)
                students.add(new_student)

                print("Student updated!")
                found = True
                break

        if not found:
            print("Student not found.")

    # Remove Student
    elif choice == "5":
        sid = input("Enter ID to remove: ")
        found = False

        for s in students:
            if s[0] == sid:
                students.remove(s)
                print("Student removed!")
                found = True
                break

        if not found:
            print("Student not found.")

    # Exit
    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")