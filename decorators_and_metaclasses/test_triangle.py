import pytest
from triangle import Point, Triangle

class TestTriangle:

    @pytest.fixture
    def example_points(self):
        return Point(0, 0), Point(0, 10), Point(10, 0)
    def test_from_points(self, example_points):
        p1, p2, p3 = example_points
        t1 = Triangle.from_points(points=example_points)
        t2 = Triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)
        assert t1 == t2

    def test_from_points2(self):
        points = [Point(1, 2), Point(3, 4), Point(5, 6)]
        with pytest.raises(ValueError) as err:
            Triangle.from_points(points=points)
        assert str(err.value) == "Points are collinear"


    def test_top(self, example_points):  # getting an attribute value
        assert Triangle.from_points(example_points).top == 10

    def test_left(self, example_points):  # getting an attribute value
        assert Triangle.from_points(example_points).left == 0

    def test_right(self, example_points):  # getting an attribute value
        assert Triangle.from_points(example_points).right == 10

    def test_bottom(self, example_points):  # getting an attribute value
        assert Triangle.from_points(example_points).bottom == 0

    def test_width(self, example_points):  # getting an attribute value
        assert Triangle.from_points(example_points).width == 10

    def test_height(self, example_points):  # getting an attribute value
        assert Triangle.from_points(example_points).height == 10

    def test_topleft(self, example_points):  # getting an attribute value
        assert Triangle.from_points(example_points).topleft == Point(0, 10)

    def test_bottomleft(self, example_points):  # getting an attribute value
        assert Triangle.from_points(example_points).bottomleft == Point(0, 0)

    def test_topright(self, example_points):  # getting an attribute value
        assert Triangle.from_points(example_points).topright == Point(10, 10)

    def test_bottomright(self, example_points):  # getting an attribute value
        assert Triangle.from_points(example_points).bottomright == Point(10, 0)

    def test_width(self, example_points):  # getting an attribute value
        assert Triangle.from_points(example_points).width == 10


    def test_height(self, example_points):  # getting an attribute value
        assert Triangle.from_points(example_points).height == 10