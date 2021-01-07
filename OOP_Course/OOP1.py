class Instructor:
    companyName = "MinionZone"

    def __init__(self, course):
        # initializer. All classes must have this function.
        # self parameter is a reference to the current instance of the class.
        self.course = course

    def PrintInfo(self):
        print("Company name : ", Instructor.companyName)


class Pets:
    # pass keyword means this class has no methods.
    pass


# instantiating a class.
object1 = Instructor("Python")
object2 = Instructor("Django")
# calling class methods using objects.
object2.PrintInfo()
object1.PrintInfo()
print(object1.course)

# remove an attribute
del object2.course
