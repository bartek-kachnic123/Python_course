import math
from points import Point

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
            raise ValueError("Points are collinear")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):       # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[{}, {}, {}]".format(self.pt1, self.pt2, self.pt3)

    def __repr__(self):       # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "{}({}, {}, {}, {}, {}, {})".format(self.__class__.__name__,
                                                   self.pt1.x, self.pt1.y,
                                                   self.pt2.x, self.pt2.y,
                                                   self.pt3.x, self.pt3.y)

    def __eq__(self, other):   # obsługa tr1 == tr2
        s = {self.pt1, self.pt2, self.pt3}
        other_s = {other.pt1, other.pt2, other.pt3}
        return s == other_s

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):          # zwraca środek trójkąta
        x = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        y = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return x, y

    def area(self):           # pole powierzchni
        return math.fabs(self.pt1.x * (self.pt2.y - self.pt3.y) +
                         self.pt2.x * (self.pt3.y - self.pt1.y) +
                         self.pt3.x * (self.pt1.y - self.pt2.y)) / 2

    def move(self, x, y):      # przesunięcie o (x, y)
        t = Triangle(self.pt1.x + x, self.pt1.y + y,
                     self.pt2.x + x, self.pt2.y + y,
                     self.pt3.x + x, self.pt3.x + y)
        return t


    def make4(self):          # zwraca krotkę czterech mniejszych
        pt1_mid = Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        pt2_mid = Point((self.pt1.x + self.pt3.x) / 2, (self.pt1.y + self.pt3.y) / 2)
        pt3_mid = Point((self.pt2.x + self.pt3.x) / 2, (self.pt2.y + self.pt3.y) / 2)

        t1_mid = Triangle(pt1_mid.x, pt1_mid.y, pt2_mid.x, pt2_mid.y, pt3_mid.x, pt3_mid.y)
        t2 = Triangle(self.pt1.x, self.pt2.y, pt1_mid.x, pt1_mid.y, pt2_mid.x, pt2_mid.y)
        t3 = Triangle(self.pt2.x, self.pt2.y, pt1_mid.x, pt1_mid.y, pt3_mid.x, pt3_mid.y)
        t4 = Triangle(self.pt3.x, self.pt3.y, pt2_mid.x, pt2_mid.y, pt3_mid.x, pt3_mid.y)

        return t1_mid, t2, t3, t4

