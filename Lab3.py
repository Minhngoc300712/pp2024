import math
import numpy as np
import curses

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
    def __init__(self, course_id=None, course_name=None, credit=None):
        self.id = course_id
        self.name = course_name
        self.credit = credit

    def input(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        credit = float(input("Enter course credit: "))
        return Course(course_id, course_name, credit)


class ClassManager:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}
        self.stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(1)
        self.stdscr.refresh()

    def __del__(self):
        curses.endwin()

    def display_menu(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Class Management System", curses.color_pair(1) | curses.A_BOLD)
        self.stdscr.addstr(2, 0, "1. Input student marks")
        self.stdscr.addstr(3, 0, "2. List courses")
        self.stdscr.addstr(4, 0, "3. List students")
        self.stdscr.addstr(5, 0, "4. Show student marks for a given course")
        self.stdscr.addstr(6, 0, "5. Quit")
        self.stdscr.addstr(7, 0, "6. Sort students by GPA")
        self.stdscr.addstr(9, 0, "Your choice (1-6): ")
        self.stdscr.refresh()

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
        rounded_mark = math.floor(mark * 10) / 10  # Round down to 1 decimal place
        self.marks[(student_id, course_id)] = rounded_mark
        print("Mark added successfully.")

    def show_student_marks(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        if (student_id, course_id) in self.marks:
            print(f"Mark for student {student_id} in course {course_id}: {self.marks[(student_id, course_id)]}")
        else:
            print("Mark not found")

    def list_courses(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "List of Courses", curses.color_pair(1) | curses.A_BOLD)
        for i, (course_id, course_info) in enumerate(self.courses.items(), start=2):
            self.stdscr.addstr(i, 0, f"{course_id}: {course_info.name} - Credit: {course_info.credit}")
        self.stdscr.refresh()
        self.stdscr.getch()

    def list_students(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "List of Students", curses.color_pair(1) | curses.A_BOLD)
        for i, (student_id, student_info) in enumerate(self.students.items(), start=2):
            self.stdscr.addstr(i, 0, f"{student_id}: {student_info.name}")
        self.stdscr.refresh()
        self.stdscr.getch()

    def calculate_average_gpa(self, student_id):
        if student_id not in self.students:
            print("Student not found.")
            return

        student_courses = [course.id for course in self.courses.values()]
        student_marks = [self.marks.get((student_id, course), 0) for course in student_courses]
        student_credits = [self.courses[course].credit for course in student_courses]

        # Calculate the weighted sum of credits and marks
        weighted_sum = np.sum(np.multiply(student_credits, student_marks))

        # Calculate the total credits
        total_credits = np.sum(student_credits)

        # Calculate the average GPA
        if total_credits > 0:
            average_gpa = weighted_sum / total_credits
            return round(average_gpa, 2)
        else:
            return 0.0

    def sort_students_by_gpa(self):
        sorted_students = sorted(self.students.items(), key=lambda x: self.calculate_average_gpa(x[0]), reverse=True)

        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Students sorted by GPA (descending)", curses.color_pair(1) | curses.A_BOLD)
        for i, (student_id, student_info) in enumerate(sorted_students, start=2):
            self.stdscr.addstr(i, 0, f"{student_id}: {student_info.name} - GPA: {self.calculate_average_gpa(student_id)}")
        self.stdscr.refresh()
        self.stdscr.getch()

    def main(self):
        self.input_students()
        self.input_courses()

        while True:
            self.display_menu()
            choice = self.stdscr.getch()

            if choice == ord('1'):
                self.input_student_mark()
            elif choice == ord('2'):
                self.list_courses()
            elif choice == ord('3'):
                self.list_students()
            elif choice == ord('4'):
                self.show_student_marks()
            elif choice == ord('5'):
                self.stdscr.addstr(11, 0, "Exiting program.")
                self.stdscr.refresh()
                break
            elif choice == ord('6'):
                self.sort_students_by_gpa()
            else:
                self.stdscr.addstr(11, 0, "Invalid choice.")
                self.stdscr.refresh()
                self.stdscr.getch()

if __name__ == "__main__":
    class_manager = ClassManager()
    class_manager.main()