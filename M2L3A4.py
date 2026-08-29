class Student:

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance methods
    def study(self, subject):
        return "{} is studying {}".format(self.name, subject)

    def play(self):
        return "{} is now playing".format(self.name)


# create the object
student1 = Student("Aarav", 14)

# call the instance methods
print(student1.study("Python"))
print(student1.play())
