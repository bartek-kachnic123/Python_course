# Kod testujący moduł.
import unittest
from rectangle import Rectangle, Point


class TestRectangle(unittest.TestCase):

    def test__init__wrong_points(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, 4)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 2, 1)

    def test__str__(self):         # "[(x1, y1), (x2, y2)]"
        self.assertEqual(str(Rectangle(1, 2, 2, 4)), "[(1, 2), (2, 4)]")

    def test__repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        self.assertEqual(repr(Rectangle(1, 2, 2, 4)), "Rectangle(1, 2, 2, 4)")

    def test__eq__(self):   # obsługa rect1 == rect2
        self.assertTrue(Rectangle(1, 1, 2, 2) == Rectangle(1, 1, 2, 2))
        self.assertTrue(Rectangle(1, 1, 2, 2) == Rectangle(2, 2, 1, 1))
        self.assertFalse(Rectangle(1, 1, 2, 2) == Rectangle(1, 1, 3, 3))

    def test__ne__(self):        # obsługa rect1 != rect2
        self.assertFalse(Rectangle(1, 1, 2, 2) != Rectangle(1, 1, 2, 2))
        self.assertFalse(Rectangle(1, 1, 2, 2) != Rectangle(2, 2, 1, 1))
        self.assertTrue(Rectangle(1, 1, 2, 2) != Rectangle(1, 1, 3, 3))

    def test_center(self):          # zwraca środek prostokąta
        self.assertEqual(Rectangle(1, 1, 2, 2).center(), Point(1.5, 1.5))

    def test_area(self):           # pole powierzchni
        self.assertAlmostEqual(Rectangle(1, 1, 2, 2).area(), 1.0, places=5)
        self.assertAlmostEqual(Rectangle(-1, -1, -2, -2).area(), 1.0, places=5)

    def test_move(self):
        self.assertEqual(Rectangle(1, 1, 2, 2).move(1, 3), Rectangle(2, 4, 3, 5))
        self.assertEqual(Rectangle(1, 1, 2, 2).move(1, -2), Rectangle(2, -1, 3, 0))


if __name__ == '__main__':
    unittest.main()
