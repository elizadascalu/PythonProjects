from abc import ABC, abstractmethod

class Shape(ABC):
    # ABC indicates that this is an abstract base class
    def __init__(self):
        super().__init__()

    # declaring a method as abstract requires a subclass to implement it
    @abstractmethod
    def calcArea(self):
        pass

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class Circle(Shape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{ \"square\": {str(self.calcArea())} }}"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


# Abstract classes can't be instantiated themselves
# g = Shape() # error

c = Circle(6)
print(c.calcArea())
print(c.toJSON())
s = Square(8)
print(s.calcArea())
