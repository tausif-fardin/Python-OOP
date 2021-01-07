class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PrintInfo(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


person1 = Person("Tausif", 21, "male")
person1.PrintInfo()


# Lawyer class inherit the person class.
class Lawyer(Person):
    def __init__(self, name, age, gender, casetype):
        # reference the parent properties or attributes.
        Person.__init__(self, name, age, gender)
        self.casetype = casetype
        self.name = name
        self.age = age
        self.gender = gender

    def PrintLawyerInfo(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


lawyer1 = Lawyer("Arik", 30, "male", "Criminal")
lawyer1.PrintLawyerInfo()
print(lawyer1.casetype)
