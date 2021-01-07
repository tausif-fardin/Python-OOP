class Cars:
    def __init__(self, speed, color):
        # __ use to set the access modifier to private
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed


ford = Cars(250, "Black")
audi = Cars(300, "Black")
bmw = Cars(320, "Black")

ford.set_speed(150)
print(ford.get_speed())
# print(ford.color)

