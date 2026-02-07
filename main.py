student_list = []

def load_data():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, grade = line.strip().split(",")
                student_list.append((name, float(grade)))
    except FileNotFoundError:
        pass

def save_data():
    with open("students.txt", "w") as file:
        for name, grade in student_list:
            file.write(f"{name},{grade}\n")

def add_new_student():
    name = input("Student name: ")
    grade = float(input("Grade: "))
    student_list.append((name, grade))
    save_data()

def show_students():
    for name, grade in student_list:
        print(f"{name} - {grade}")

def show_average():
    if student_list:
        avg = sum(g for _, g in student_list) / len(student_list)
        print("Average:", round(avg, 2))
    else:
        print("No students yet.")

def menu():
    load_data()
    while True:
        print("\n1. Add New Student\n2. Show Students\n3. Show Average\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_new_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            show_average()
        elif choice == "4":
            break

menu()
