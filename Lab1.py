def input_student():
    student_id = input("student ID: ")
    student_name = input("student name: ")
    student_dob = input("student Date of Birth(dd/mm/yy): ")
    return {'id': student_id, 'name': student_name, 'dob': student_dob}

def input_course():
    course_id = input("course ID: ")
    course_name = input("course name: ")
    return {'id': course_id, 'name': course_name}

def input_student_mark(marks):
    student_id = input("student ID: ")
    course_id = input("course ID: ")
    mark = float(input("mark: "))
    
    marks[(student_id, course_id)] = mark
    print("Mark added successfully.")

def list_courses(courses):
    print("List of Courses:")
    for course_id, course_info in courses.items():
        print(f"{course_id}: {course_info['name']}")

def list_students(students):
    print("List of Students:")
    for student_id, student_info in students.items():
        print(f"{student_id}: {student_info['name']}")

def show_student_marks(marks):
    student_id = input("student ID: ")
    course_id = input("course ID: ")
    
    if (student_id, course_id) in marks:
        print(f"Mark for student {student_id} in course {course_id}: {marks[(student_id, course_id)]}")
    else:
        print("Mark not found")

def main():
    students = {}
    courses = {}
    marks = {}

    num_students = int(input("the number of students in the class: "))
    for _ in range(num_students):
        student_info = input_student()
        students[student_info['id']] = student_info

    num_courses = int(input("the number of courses: "))
    for _ in range(num_courses):
        course_info = input_course()
        courses[course_info['id']] = course_info

    while True:
        print("\n1. Input student marks")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a given course")
        print("5. Quit")

        choice = input("your choice (1-5): ")

        if choice == '1':
            input_student_mark(marks)
        elif choice == '2':
            list_courses(courses)
        elif choice == '3':
            list_students(students)
        elif choice == '4':
            show_student_marks(marks)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

main()