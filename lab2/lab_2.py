from abc import ABC, abstractmethod
import math


class Geom_Figure(ABC):
    @abstractmethod
    def square(self):
        pass


class Figure_Colour:
    def __init__(self):
        self._color = None

    @property
    def colorproperty(self):
        return self._color

    @colorproperty.setter
    def colorproperty(self, value):
        self._color = value


class Rectangle(Geom_Figure):
    figure_type = "Rectangle"

    @classmethod
    def get_type(cls):
        return cls.figure_type

    def __init__(self, width, height, colour):
        self._width = width
        self._height = height
        self.fc = Figure_Colour()
        self.fc.colorproperty = colour

    def square(self):
        return self._width * self._height

    def __repr__(self):
        return "{}, width = {}, height = {}, colour = {}, square = {}".format(self.get_type(),
                                                                           self._width, self._height,
                                                                           self.fc.colorproperty,
                                                                           self.square())


class Circle(Geom_Figure):
    figure_type = "Circle"

    @classmethod
    def get_type(cls):
        return cls.figure_type

    def __init__(self, radius, colour):
        self._radius = radius
        self.fc = Figure_Colour()
        self.fc.colorproperty = colour

    def square(self):
        return ((self._radius) ** 2) * math.pi

    def __repr__(self):
        return "{}, radius = {}, colour = {}, square = {}".format(self.get_type(),
                                                               self._radius, self.fc.colorproperty,
                                                               self.square())


class Square(Rectangle):
    figure_type = "Square"

    @classmethod
    def get_type(cls):
        return cls.figure_type

    def __init__(self, side, colour):
        self._side = side
        super().__init__(self._side, self._side, colour)

    def __repr__(self):
        return "{}, side = {}, colour = {}, square = {}".format(self.get_type(),
                                                             self._side, self.fc.colorproperty,
                                                             self.square())


def main():
    r = Rectangle(3, 2, "Blue", )
    c = Circle(5, "Green")
    s = Square(5, "Red", )
    print(r)
    print(c)
    print(s)


if __name__ == "__main__":
    main()
