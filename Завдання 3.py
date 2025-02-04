class Student:
    def __init__(self, name, age, faculty, course):
        self.name = name
        self.age = age
        self.faculty = faculty
        self.course = course

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.faculty}, {self.course} course"

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("The student list is empty.")
        else:
            print("\nStudent List:")
            for student in self.students:
                print(student)

    def find_by_faculty(self, faculty):
        result = [student for student in self.students if student.faculty.lower() == faculty.lower()]
        if result:
            print(f"\nStudents from the {faculty} faculty:")
            for student in result:
                print(student)
        else:
            print(f"\nNo students found in the {faculty} faculty.")

    def find_by_course(self, course):
        result = [student for student in self.students if student.course == course]
        if result:
            print(f"\nStudents in course {course}:")
            for student in result:
                print(student)
        else:
            print(f"\nNo students found in course {course}.")

    def delete_student(self, name):
        student_to_remove = None
        for student in self.students:
            if student.name.lower() == name.lower():
                student_to_remove = student
                break
        
        if student_to_remove:
            self.students.remove(student_to_remove)
            print(f"Student {name} has been removed from the list.")
        else:
            print(f"Student with the name {name} was not found.")

def main():
    student_list = StudentList()

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Display Student List")
        print("3. Search Students by Faculty")
        print("4. Search Students by Course")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose an action (1-6): ")

        if choice == "1":
            name = input("Enter the student's name: ")
            
            while True:
                try:
                    age = int(input("Enter the student's age: "))
                    if age <= 0:
                        print("Age must be a positive number. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Age must be an integer. Please try again.")
            
            faculty = input("Enter the student's faculty: ")
            
            while True:
                try:
                    course = int(input("Enter the student's course: "))
                    if course <= 0:
                        print("Course must be a positive number. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Course must be an integer. Please try again.")
            
            student = Student(name, age, faculty, course)
            student_list.add_student(student)
            print("Student has been added to the list.")
        
        elif choice == "2":
            student_list.display_students()

        elif choice == "3":
            faculty = input("Enter the faculty name for the search: ")
            student_list.find_by_faculty(faculty)

        elif choice == "4":
            while True:
                try:
                    course = int(input("Enter the course for the search: "))
                    if course <= 0:
                        print("Course must be a positive number. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Course must be an integer. Please try again.")
            
            student_list.find_by_course(course)

        elif choice == "5":
            name_to_delete = input("Enter the student's name to delete: ")
            student_list.delete_student(name_to_delete)

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
