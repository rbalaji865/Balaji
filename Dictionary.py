students = {'balaji' : 100, 'sridevi' : 101, 'vishu' : 102}

students_name_input = input("Enter student name: ")

if students_name_input in students:
    marks = students[students_name_input]
    print(f"The marks for {students_name_input} is {marks}")
else:
    print(f"Student not found")

