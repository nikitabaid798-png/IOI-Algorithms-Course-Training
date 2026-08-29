# ---- Student Details using Inheritance and Abstraction ----

from abc import ABC, abstractmethod


# Parent class
class Student(ABC):

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Abstract method
    @abstractmethod
    def display_details(self):
        pass


# Child class
class SchoolStudent(Student):

    def __init__(self, name, roll_no, grade):
        super().__init__(name, roll_no)
        self.grade = grade

    # Implement abstract method
    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Grade:", self.grade)


# Create an object
student1 = SchoolStudent("Riya", 15, 8)

# Display student details
student1.display_details()
