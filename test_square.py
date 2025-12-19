import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(10), 100)
        self.assertEqual(area(1), 1)

    def test_area_float(self):
        self.assertEqual(area(2.5), 6.25)
        self.assertEqual(area(0.5), 0.25)
        self.assertEqual(area(3.5), 12.25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_large_number(self):
        self.assertEqual(area(1000), 1000000)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5)
        with self.assertRaises(ValueError):
            area(-0.1)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(10), 40)
        self.assertEqual(perimeter(1), 4)

    def test_perimeter_float(self):
        self.assertEqual(perimeter(2.5), 10.0)
        self.assertEqual(perimeter(0.75), 3.0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_large_number(self):
        self.assertEqual(perimeter(500), 2000)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-3)
        with self.assertRaises(ValueError):
            perimeter(-2.5)


if __name__ == '__main__':
    unittest.main()