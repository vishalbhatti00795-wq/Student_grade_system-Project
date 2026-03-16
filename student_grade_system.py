student_grades = { }

# Add a new student
def add_student(name,grade):
    student_grades[name] = grade
    print(f"Added {name} with {grade} grade.")

# Update a student
def update_student(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are updated {grade}.")

    else:
        print(f"Student {name} does not exist.")

# Delete a Student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been deleted successfully.")

    else:
        print(f"Student {name} does not exist.")

# View all students
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")

    else:
        print("Student does not exist.")

def main():
    while True:

        print('\n-----Student Grade System-----')
        print('1. Add student')
        print('2. Update student')
        print('3. Delete student')
        print('4. Display all students')
        print('5. Exit')

        choice = input('Enter your choice(1/2/3/4/5): ')
        if choice == '1':
           name = input('Enter student name: ')
           grade = input('Enter student grade: ')
           add_student(name,grade)

        elif choice == '2':
            name = input('Enter student name: ')
            grade = input('Enter student grade: ')
            update_student(name,grade)

        elif choice == '3':
            name = input('Enter student name: ')
            delete_student(name)

        elif choice == '4':
            display_all_students()

        elif choice == '5':
            print("Thank you for using this program")
            break

        else:
            print("Invalid Choice!")

main()