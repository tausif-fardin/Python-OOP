from abc import ABC, abstractmethod


class Shape(ABC):
    # a decorator allows you to add new functionality to an existing object without modifying its structure.
    @abstractmethod  # this will create abstraction in a class
    # a function inside a class is called method
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


mysquare = Square(12)
print(mysquare.area())
print(mysquare.perimeter())

