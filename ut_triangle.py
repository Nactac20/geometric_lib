import unittest
from triangle import*
class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
       test_d = ((1,3,1.5), (-2,0,'impossible to calculate area'), (3.5,4,7), (0,2.5,'impossible to calculate area'), (2.5,-6,'error'), (0,0,'impossible to calculate area'), (True, 1, 'error'), ('fgd', -2, 'error'))
       for x,y,k in test_d:
          res = area(x,y)
          self.assertEqual(res, k)
    def test_triangle_perimeter(self):
        test_d = ((1,3,5,'not triangle'), (-10, 0, 5.4, 'impossible to calculate perimeter'),(0,0,0,'impossible to calculate perimeter'),(3,5,2,10), (2.5, 3.5, 6, 12),(True, 1, -1, 'error'), ('fgd', 8, -9, 'error'))
        for x,y,z,k in test_d:
            res = perimeter(x,y,z)
            self.assertEqual(res, k)