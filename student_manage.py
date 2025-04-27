students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))
    students.append({'roll': roll, 'name': name, 'age': age, 'marks': marks})
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found!")
        return
    for student in students:
        print(f"Roll: {student['roll']}, Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

def search_student():
    roll = input("Enter Roll Number to Search: ")
    for student in students:
        if student['roll'] == roll:
            print(f"Found: {student}")
            return
    print("Student not found!")

def update_student():
    roll = input("Enter Roll Number to Update: ")
    for student in students:
        if student['roll'] == roll:
            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            marks = float(input("Enter New Marks: "))
            student['name'] = name
            student['age'] = age
            student['marks'] = marks
            print("Student updated successfully!")
            return
    print("Student not found!")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    for student in students:
        if student['roll'] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found!")

def save_to_file():
    with open('students.txt', 'w') as file:
        for student in students:
            file.write(f"{student['roll']},{student['name']},{student['age']},{student['marks']}\n")

def load_from_file():
    try:
        with open('students.txt', 'r') as file:
            for line in file:
                roll, name, age, marks = line.strip().split(',')
                students.append({'roll': roll, 'name': name, 'age': int(age), 'marks': float(marks)})
    except FileNotFoundError:
        pass

# --- Main Menu ---

load_from_file()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        save_to_file()
        print("Data saved. Exiting...")
        break
    else:
        print("Invalid Choice. Try Again!")
