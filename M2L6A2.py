class Student:
    def __init__(self, name, marks):
        self.__name = name       # private — locked inside the class
        self.__marks = marks     # private — locked inside the class

    def get_marks(self):         # approved way to READ the marks
        return self.__marks

    def set_marks(self, new_marks):   # approved way to CHANGE the marks
        if new_marks >= 0:
            self.__marks = new_marks
