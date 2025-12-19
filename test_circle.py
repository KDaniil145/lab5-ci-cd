import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(5), math.pi * 25)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5), math.pi * 6.25)
        self.assertAlmostEqual(area(0.5), math.pi * 0.25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_large_number(self):
        self.assertAlmostEqual(area(1000), math.pi * 1000000)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5)
        with self.assertRaises(ValueError):
            area(-0.1)

    def test_perimeter_normal(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(10), 20 * math.pi)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5), 5 * math.pi)
        self.assertAlmostEqual(perimeter(0.75), 1.5 * math.pi)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_large_number(self):
        self.assertAlmostEqual(perimeter(500), 1000 * math.pi)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-3)
        with self.assertRaises(ValueError):
            perimeter(-2.5)


if __name__ == '__main__':
    unittest.main()