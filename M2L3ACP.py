# ---- Robot Introduction ----

class Robot:

    # instance attribute
    def __init__(self, name):
        self.name = name

    # instance method
    def introduce(self):
        print("Hello! My name is", self.name)


# create two robot objects
robot1 = Robot("Tom")
robot2 = Robot("Jerry")

# make the robots introduce themselves
robot1.introduce()
robot2.introduce()
