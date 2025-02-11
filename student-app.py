from pathlib import Path

class Student:
  def __init__(self, id, firstName, lastName):
    self.id = id
    self.firstName = firstName
    self.lastName = lastName

def main():
    studentArray = []
    p = Path(__file__).with_name('student-data.txt')
    with p.open('r') as file:
        for line in file:
            data = line.split('|')
            student = Student(data[0].strip(), data[1].strip(), data[2].strip())
            studentArray.append(student)

    print("Welcome to CS540 Student Info App.")
    inputValue = input("Enter student id: ")

    search_student(studentArray, inputValue)

    print("Goodbye!")

def search_student(studentArray, inputValue):
    found = False
    for student in studentArray:
        if inputValue == student.id:
            found = True
            print_student_info(student)

    if not found:
        print("Student not found.")

def print_student_info(student):
    print("ID: {0}. First Name: {1}. Last Name: {2} ".format( student.id, student.firstName, student.lastName))

if __name__ == '__main__':
    main()
