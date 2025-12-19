import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    # Тесты для area()
    def test_area_normal(self):
        self.assertEqual(area(10, 5), 25)
        self.assertEqual(area(6, 4), 12)
        self.assertEqual(area(8, 3), 12)

    def test_area_float(self):
        self.assertEqual(area(2.5, 4.0), 5.0)
        self.assertEqual(area(3.3, 2.2), 3.63)
        self.assertEqual(area(0.5, 2), 0.5)

    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_area_large_numbers(self):
        self.assertEqual(area(1000, 500), 250000)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5, 10)
        with self.assertRaises(ValueError):
            area(5, -10)
        with self.assertRaises(ValueError):
            area(-5, -10)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(10, 10, 10), 30)
        self.assertEqual(perimeter(5, 6, 7), 18)

    def test_perimeter_float(self):
        self.assertEqual(perimeter(2.5, 3.5, 4.5), 10.5)
        self.assertEqual(perimeter(1.1, 2.2, 3.3), 6.6)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 5, 5), 10)
        self.assertEqual(perimeter(5, 0, 5), 10)
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_equilateral(self):
        self.assertEqual(perimeter(7, 7, 7), 21)

    def test_perimeter_large_numbers(self):
        self.assertEqual(perimeter(100, 200, 300), 600)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            perimeter(-3, -4, -5)


if __name__ == '__main__':
    unittest.main()