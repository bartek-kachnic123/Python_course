import unittest
from points import Point


class TestPoint(unittest.TestCase):
    def test__str__(self):        # zwraca string "(x, y)"
        self.assertEqual(str(Point(1, 2)), "(1, 2)")

    def test__repr__(self):        # zwraca string "Point(x, y)"
        self.assertEqual(repr(Point(1, 2)), "Point(1, 2)")
    def test__eq__(self):   # obsługa point1 == point2
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertFalse(Point(1, 2) == Point(1, 3))

    def test__ne__(self):
        self.assertTrue(Point(1, 2) != Point(1, 3))
        self.assertFalse(Point(1, 2) != Point(1, 2))

    def test__add__(self):  # v1 + v2
        self.assertEqual(Point(1, 3) + Point(1, 2), Point(2, 5))
        self.assertEqual(Point(-1, 3) + Point(1, -2), Point(0, 1))

    def test__sub__(self):  # v1 - v2
        self.assertEqual(Point(1, 2) - Point(1, 2), Point(0, 0))
        self.assertEqual(Point(1, 2) - Point(-1, -2), Point(2, 4))

    def test__mul__(self):
        self.assertEqual(Point(1, 3) * Point(1, 4), 13)
        self.assertEqual(Point(1, -3) * Point(1, 4), -11)

    def test_cross(self):
        self.assertEqual(Point(1, 5).cross(Point(3, 4)), 4-15)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)

    def test__hash__(self):
        self.assertEqual(hash(Point(1, 2)), hash((1, 2)))


if __name__ == '__main__':
    unittest.main()