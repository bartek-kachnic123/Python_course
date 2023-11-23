from points import Point
from math import fabs
class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 == x2 or y1 == y2:
            raise ValueError("Points must be different and cant be on same x and y axis")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)


    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return "[{}, {}]".format(self.pt1, self.pt2)

    def __repr__(self):       # "Rectangle(x1, y1, x2, y2)"
        return "{}({}, {}, {}, {})".format(self.__class__.__name__,
                                           self.pt1.x, self.pt1.y,
                                           self.pt2.x, self.pt2.y)

    def __eq__(self, other):  # obsługa rect1 == rect2
        return ((self.pt1 == other.pt1 and self.pt2 == other.pt2) or
                (self.pt1 == other.pt2 and self.pt2 == other.pt1))

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        x = (self.pt1.x + self.pt2.x) / 2
        y = (self.pt1.y + self.pt2.y) / 2
        return Point(x, y)

    def area(self):         # pole powierzchni
        x = fabs(self.pt1.x - self.pt2.x)
        y = fabs(self.pt1.y - self.pt2.y)
        return x * y

    def move(self, x, y):      # przesunięcie o (x, y)
        p = Point(x, y)
        self.pt1 += p
        self.pt2 += p
        return self
