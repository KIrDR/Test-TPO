import unittest
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
        self.assertFalse(is_triangle(-1, 4, 5))
        self.assertFalse(is_triangle(3, -2, 5))
        self.assertFalse(is_triangle(3, 4, -6))
        self.assertFalse(is_triangle(0, 4, 5))
        self.assertFalse(is_triangle(3, 0, 5))
        self.assertFalse(is_triangle(3, 4, 0))

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 12, 13), 30)
        self.assertEqual(perimeter(8, 15, 17), 40)
        self.assertAlmostEqual(perimeter(3.5, 4.5, 5.5), 13.5)
        self.assertAlmostEqual(perimeter(5.25, 12.75, 13.75), 31.75)
        self.assertAlmostEqual(perimeter(8.3, 15.7, 17.2), 41.2)

    def test_area(self):
        self.assertAlmostEqual(area(3, 4, 5), 6)
        self.assertAlmostEqual(area(5, 12, 13), 30)
        self.assertAlmostEqual(area(8, 15, 17), 60)
        self.assertAlmostEqual(area(3.5, 4.5, 5.5), 7.8549, places=4)
        self.assertAlmostEqual(area(5.25, 12.75, 13.75), 33.468, places=3)
        self.assertAlmostEqual(area(8.3, 15.7, 17.2), 64.972, places=3)

    def test_inradius(self):
        self.assertAlmostEqual(inradius(3, 4, 5), 1)
        self.assertAlmostEqual(inradius(5, 12, 13), 2)
        self.assertAlmostEqual(inradius(8, 15, 17), 3)
        self.assertAlmostEqual(inradius(3.5, 4.5, 5.5), 1.1637, places=4)
        self.assertAlmostEqual(inradius(5.25, 12.75, 13.75), 2.1082, places=4)
        self.assertAlmostEqual(inradius(8.3, 15.7, 17.2), 3.154, places=3)

    def test_circumradius(self):
        self.assertAlmostEqual(circumradius(3, 4, 5), 2.5)
        self.assertAlmostEqual(circumradius(5, 12, 13), 6.5)
        self.assertAlmostEqual(circumradius(8, 15, 17), 8.5)
        self.assertAlmostEqual(circumradius(3.5, 4.5, 5.5), 2.7570, places=4)
        self.assertAlmostEqual(circumradius(5.25, 12.75, 13.75), 6.8752, places=4)
        self.assertAlmostEqual(circumradius(8.3, 15.7, 17.2), 8.6243, places=4)

    def test_is_triangle_all_equal_sides(self):
        self.assertTrue(is_triangle(5, 5, 5))

    def test_is_triangle_two_equal_sides(self):
        self.assertTrue(is_triangle(4, 4, 5))

    def test_is_triangle_invalid_negative_side(self):
        self.assertFalse(is_triangle(-3, 4, 5))

    def test_is_triangle_invalid_zero_side(self):
        self.assertFalse(is_triangle(0, 4, 5))
if __name__ == '__main__':
    unittest.main()
