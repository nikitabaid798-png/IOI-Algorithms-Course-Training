class Animal:                     # parent class
    def display(self):
        print("I am an animal.")

class Dog(Animal):                # child class — inherits from Animal
    pass

d = Dog()
d.display()   # Output: I am an animal.
# Dog defined nothing — it inherited display() from Animal
