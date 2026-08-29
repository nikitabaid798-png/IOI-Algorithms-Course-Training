class Student:

    # class attribute
    category = "Learner"

    # instance attributes
    def __init__(self, student_name, student_age):
        self.name = student_name
        self.age = student_age


# create objects of the Student class
student1 = Student("Riya", 14)
student2 = Student("Kabir", 15)

# access the class attribute
print("{} is a {}".format(student1.name, student1.category))
print("{} is also a {}".format(student2.name, student2.category))

# access the instance attributes
print("{} is {} years old".format(student1.name, student1.age))
print("{} is {} years old".format(student2.name, student2.age))
