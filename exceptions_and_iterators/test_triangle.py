import unittest
from triangle import Triangle

class TestTriangle(unittest.TestCase):

    def test__init__(self):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        with self.assertRaises(ValueError):
            Triangle(1, 1, 1, 2, 1, 2)
        with self.assertRaises(ValueError):
            Triangle(1,2, 3, 2, 2, 2)

    def test__str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        self.assertEqual(str(Triangle(1, 2, 3, 4, 5, 6)),
                         "[(1, 2), (3, 4), (5, 6)]")

    def test__repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        self.assertEqual(repr(Triangle(1, 2, 3, 4, 5, 6)),
                         "Triangle(1, 2, 3, 4, 5, 6)")

    def test__eq__(self):  # obsługa tr1 == tr2
        t1 = Triangle(1, 2, 3, 4, 5, 6)
        t2 = Triangle(1, 2, 5, 6, 3, 4)
        t3 = Triangle(1, 2, 3, 4, 5, 9)
        self.assertTrue(t1 == t2)
        self.assertFalse(t1 == t3)


    def test__ne__(self):        # obsługa tr1 != tr2
        t1 = Triangle(1, 2, 3, 4, 5, 6)
        t2 = Triangle(1, 2, 5, 6, 3, 4)
        t3 = Triangle(1, 2, 3, 4, 5, 9)
        self.assertFalse(t1 != t2)
        self.assertTrue(t1 != t3)

    def test_center(self):          # zwraca środek trójkąta
        t1 = Triangle(0, 0, 6, 0, 3, 6)
        self.assertEqual(t1.center(), (3, 2))

    def test_area(self):          # pole powierzchni
        t1 = Triangle(0, 0, 0, 6, 3, 0)
        self.assertEqual(t1.area(), 9)

    def test_move(self):      # przesunięcie o (x, y)
        t1 = Triangle(1, 3, 5, 2, 1, 1)
        t2 = Triangle(2, 5, 6, 4, 2, 3)
        self.assertEqual(t1.move(1, 2), t2)

    def test_make4(self):          # zwraca krotkę czterech mniejszych
        t = Triangle(0, 0, 6, 0, 3, 6)
        t1 = Triangle(0, 0, 1.5, 3, 3, 0)
        t2 = Triangle(3, 0, 1.5, 3, 4.5, 3)
        t3 = Triangle(6, 0, 3, 0, 4.5, 3)
        t4 = Triangle(3, 6, 1.5, 3, 4.5, 3)
        triangles = (t1, t2, t3, t4)
        t_triangles = t.make4()
        for triangle in triangles:
            self.assertTrue(triangle in t_triangles)


if __name__ == "__main__":
    unittest.main()