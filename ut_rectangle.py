import unittest
from rectangle import*
class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area(self):
       test_d = ((3,4,12), (-2,0,'impossible to calculate area'), (2.5,6.25,15.625), (0,0,'impossible to calculate area'), (-2.5,-1,'error'), (True,-1,'error'), ('fgd', 1, 'error'))
       for x,y,k in test_d:
          res = area(x,y)
          self.assertEqual(res, k)
    def test_rectangle_perimeter(self):
        test_d = ((1,4,10), (-10, 6,'error'), (3.5,12,31),(0,0,'impossible to calculate perimeter'), (-2.5,-4,'error'), (True, -1, 'error'), ('fgd', 1, 'error'))
        for x,y,k in test_d:
            res = perimeter(x,y)
            self.assertEqual(res, k)