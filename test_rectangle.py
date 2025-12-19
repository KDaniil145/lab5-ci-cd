import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(area(10, 5), 50)
        self.assertEqual(area(3, 7), 21)

    def test_area_float(self):
        self.assertEqual(area(2.5, 4), 10.0)
        self.assertEqual(area(3.3, 2.2), 7.26)

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(0, 0), 0)

    def test_area_square(self):
        self.assertEqual(area(10, 10), 100)
        self.assertEqual(area(5, 5), 25)

    def test_area_large_numbers(self):
        self.assertEqual(area(1000, 500), 500000)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5, 10)
        with self.assertRaises(ValueError):
            area(5, -10)
        with self.assertRaises(ValueError):
            area(-5, -10)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(10, 5), 30)
        self.assertEqual(perimeter(3, 7), 20)

    def test_perimeter_float(self):
        self.assertEqual(perimeter(2.5, 4.5), 14.0)
        self.assertEqual(perimeter(1.1, 2.1), 6.4)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(10, 0), 20)
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_large_numbers(self):
        self.assertEqual(perimeter(1000, 500), 3000)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 10)
        with self.assertRaises(ValueError):
            perimeter(5, -10)


if __name__ == '__main__':
    unittest.main()