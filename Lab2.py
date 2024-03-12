class Student:
    def __init__(self, student_id=None, student_name=None, student_dob=None):
        self.id = student_id
        self.name = student_name
        self.dob = student_dob

    def input(self):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student Date of Birth (dd/mm/yy): ")
        return Student(student_id, student_name, student_dob)


class Course:
    def __init__(self, course_id=None, course_name=None):
        self.id = course_id
        self.name = course_name

    def input(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        return Course(course_id, course_name)


class ClassManager:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

    def input_students(self):
        num_students = int(input("Enter the number of students in the class: "))
        for _ in range(num_students):
            student = Student().input()
            self.students[student.id] = student

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course = Course().input()
            self.courses[course.id] = course

    def input_student_mark(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        mark = float(input("Enter mark: "))
        self.marks[(student_id, course_id)] = mark
        print("Mark added successfully.")

    def show_student_marks(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        if (student_id, course_id) in self.marks:
            print(f"Mark for student {student_id} in course {course_id}: {self.marks[(student_id, course_id)]}")
        else:
            print("Mark not found")

    def list_courses(self):
        print("List of Courses:")
        for course_id, course_info in self.courses.items():
            print(f"{course_id}: {course_info.name}")

    def list_students(self):
        print("List of Students:")
        for student_id, student_info in self.students.items():
            print(f"{student_id}: {student_info.name}")

    def main(self):
        self.input_students()
        self.input_courses()

        while True:
            print("\n1. Input student marks")
            print("2. List courses")
            print("3. List students")
            print("4. Show student marks for a given course")
            print("5. Quit")

            choice = input("Your choice (1-5): ")

            if choice == '1':
                self.input_student_mark()
            elif choice == '2':
                self.list_courses()
            elif choice == '3':
                self.list_students()
            elif choice == '4':
                self.show_student_marks()
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    class_manager = ClassManager()
    class_manager.main()