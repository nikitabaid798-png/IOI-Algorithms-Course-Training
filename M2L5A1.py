# ---- Employee Details using Inheritance and Abstraction ----

from abc import ABC, abstractmethod


# Parent class
class Employee(ABC):

    # Constructor
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    # Abstract method
    @abstractmethod
    def display_details(self):
        pass


# Child class
class Manager(Employee):

    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    # Implement abstract method
    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)


# Create an object
employee1 = Manager("Riya", 101, "Technology")

# Display employee details
employee1.display_details()
