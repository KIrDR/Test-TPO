import unittest
import math

from main import is_triangle, perimeter, area, inradius, circumradius


class TestTriangleFunctions(unittest.TestCase):

    def test_is_triangle_valid(self):
        self.assertTrue(is_triangle(3, 4, 5))
        self.assertTrue(is_triangle(5, 12, 13))
        self.assertTrue(is_triangle(8, 15, 17))

    def test_is_triangle_invalid(self):
        self.assertFalse(is_triangle(1, 2, 10))
        self.assertFalse(is_triangle(5, 5, 12))
        self.assertFalse(is_triangle(7, 3, 2))

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 12, 13), 30)
        self.assertEqual(perimeter(8, 15, 17), 40)

    def test_area(self):
        self.assertAlmostEqual(area(3, 4, 5), 6)
        self.assertAlmostEqual(area(5, 12, 13), 30)
        self.assertAlmostEqual(area(8, 15, 17), 60)

    def test_inradius(self):
        self.assertAlmostEqual(inradius(3, 4, 5), 1)
        self.assertAlmostEqual(inradius(5, 12, 13), 2)
        self.assertAlmostEqual(inradius(8, 15, 17), 3)

    def test_circumradius(self):
        self.assertAlmostEqual(circumradius(3, 4, 5), 2.5)
        self.assertAlmostEqual(circumradius(5, 12, 13), 6.5)
        self.assertAlmostEqual(circumradius(8, 15, 17), 8.5)

###############

    def test_is_triangle_valid(self):
        self.assertTrue(is_triangle(3, 4, 5))
        self.assertTrue(is_triangle(5, 12, 13))
        self.assertTrue(is_triangle(8, 15, 17))

    def test_is_triangle_invalid(self):
        self.assertFalse(is_triangle(1, 2, 10))
        self.assertFalse(is_triangle(5, 5, 12))
        self.assertFalse(is_triangle(7, 3, 2))

    def test_perimeter_integer(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 12, 13), 30)
        self.assertEqual(perimeter(8, 15, 17), 40)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(3.5, 4.5, 5.5), 13.5)
        self.assertAlmostEqual(perimeter(5.25, 12.75, 13.75), 31.75)
        self.assertAlmostEqual(perimeter(8.3, 15.7, 17.2), 41.2)

    def test_area_integer(self):
        self.assertAlmostEqual(area(3, 4, 5), 6)
        self.assertAlmostEqual(area(5, 12, 13), 30)
        self.assertAlmostEqual(area(8, 15, 17), 60)

    def test_area_float(self):
        self.assertAlmostEqual(area(3.5, 4.5, 5.5), 7.854885024620029, places=2)
        self.assertAlmostEqual(area(5.25, 12.75, 13.75), 33.467695915940716, places=1)
        self.assertAlmostEqual(area(8.3, 15.7, 17.2), 64.97161534085484, places=2)

    def test_inradius_negative(self):
        self.assertAlmostEqual(inradius(-3, 4, 5),
                               -1)  # Отрицательные значения не имеют смысла для радиуса, тут можно подставить любое отрицательное значение.
        self.assertAlmostEqual(inradius(5, -12, 13), -1)
        self.assertAlmostEqual(inradius(8, 15, -17), -1)

    def test_circumradius_negative(self):
        self.assertAlmostEqual(circumradius(-3, 4, 5), -1)
        self.assertAlmostEqual(circumradius(5, -12, 13), -1)
        self.assertAlmostEqual(circumradius(8, 15, -17), -1)

    def test_inradius_float(self):
        self.assertAlmostEqual(inradius(3.5, 4.5, 5.5), 1.1636866703140785)
        self.assertAlmostEqual(inradius(5.25, 12.75, 13.75), 2.1082013175395726)
        self.assertAlmostEqual(inradius(8.3, 15.7, 17.2), 3.1539619097502345, places=2)

    def test_circumradius_float(self):
        self.assertAlmostEqual(circumradius(3.5, 4.5, 5.5), 2.7570422650518167, places=2)
        self.assertAlmostEqual(circumradius(5.25, 12.75, 13.75),  6.875216532023172)
        self.assertAlmostEqual(circumradius(8.3, 15.7, 17.2), 8.624273801111062, places=2)

    import unittest
    from main import is_triangle, perimeter, area, inradius, circumradius

    class TestTriangleFunctions(unittest.TestCase):

        def test_is_triangle_negative(self):
            self.assertFalse(is_triangle(-1, 4, 5))
            self.assertFalse(is_triangle(3, -2, 5))
            self.assertFalse(is_triangle(3, 4, -6))

        def test_is_triangle_zero(self):
            self.assertFalse(is_triangle(0, 4, 5))
            self.assertFalse(is_triangle(3, 0, 5))
            self.assertFalse(is_triangle(3, 4, 0))

        def test_perimeter_negative(self):
            self.assertEqual(perimeter(-3, 4, 5), -1)
            self.assertEqual(perimeter(3, -4, 5), -1)
            self.assertEqual(perimeter(3, 4, -5), -1)

        def test_perimeter_zero(self):
            self.assertEqual(perimeter(0, 4, 5), -1)
            self.assertEqual(perimeter(3, 0, 5), -1)
            self.assertEqual(perimeter(3, 4, 0), -1)

        def test_area_negative(self):
            self.assertEqual(area(-3, 4, 5), -1)
            self.assertEqual(area(3, -4, 5), -1)
            self.assertEqual(area(3, 4, -5), -1)

        def test_area_zero(self):
            self.assertEqual(area(0, 4, 5), -1)
            self.assertEqual(area(3, 0, 5), -1)
            self.assertEqual(area(3, 4, 0), -1)

        def test_inradius_negative(self):
            self.assertEqual(inradius(-3, 4, 5), -2)
            self.assertEqual(inradius(3, -4, 5), -2)
            self.assertEqual(inradius(3, 4, -5), -2)

        def test_inradius_zero(self):
            self.assertEqual(inradius(0, 4, 5), -2)
            self.assertEqual(inradius(3, 0, 5), -2)
            self.assertEqual(inradius(3, 4, 0), -2)

        def test_circumradius_negative(self):
            self.assertEqual(circumradius(-3, 4, 5), -2)
            self.assertEqual(circumradius(3, -4, 5), -2)
            self.assertEqual(circumradius(3, 4, -5), -2)

        def test_circumradius_zero(self):
            self.assertEqual(circumradius(0, 4, 5), -2)
            self.assertEqual(circumradius(3, 0, 5), -2)
            self.assertEqual(circumradius(3, 4, 0), -2)

    if __name__ == '__main__':
        unittest.main()


if __name__ == '__main__':
    unittest.main()
