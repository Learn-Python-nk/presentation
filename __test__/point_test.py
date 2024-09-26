import unittest
from model.point import Point


class Test_Point(unittest.TestCase):
    def test_default_properties_of_point(self):
        point = Point(10, 20)

        self.assertEqual(point.x, 10)
        self.assertEqual(point.y, 20)

    def test_set_x_property(self):
        point = Point(10, 10)

        self.assertEqual(point.x, 10)

        point.x = 20

        self.assertEqual(point.x, 20)

    def test_set_y_property(self):
        point = Point(10, 10)

        self.assertEqual(point.y, 10)

        point.y = 20

        self.assertEqual(point.y, 20)

    def test_invalid_set_x_property(self):
        point = Point(10, 10)

        with self.assertRaises(ValueError) as excinfo:
            point.x = "invalid"

        self.assertEqual(str(excinfo.exception), "x must be a number.")

    def test_invalid_set_y_property(self):
        point = Point(10, 10)

        with self.assertRaises(ValueError) as excinfo:
            point.y = "invalid"

        self.assertEqual(str(excinfo.exception), "y must be a number.")
