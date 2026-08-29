# ---- Constructor and Destructor ----

class Student:

    # Constructor
    def __init__(self, name):
        self.name = name
        print("Student created:", self.name)

    # Destructor
    def __del__(self):
        print("Student removed:", self.name)


# Create an object
student1 = Student("Aarav")

print("Student name:", student1.name)

# Delete the object
del student1
