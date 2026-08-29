class Student:
    grade = 9
    name = "Aarav"

    def introduction(self):
        print("Hello! I am a student.")

    def details(self):
        print("My name is", self.name)
        print("I am studying in Grade", self.grade)

student1 = Student()
student1.introduction()
student1.details()
