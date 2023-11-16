import unittest
from square import*
class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
       test_d = ((3,9), (-2,'error'), (2.5,6.25), (0,'impossible to calculate area'), (True, 'error'), ('fgd', 'error'))
       for x,k in test_d:
          res = area(x)
          self.assertEqual(res, k)
    def test_square_perimeter(self):
        test_d = ((3,12), (-2,'error'), (2.5,10),(0,'impossible to calculate perimeter'), (True, 'error'), ('fgd', 'error'))
        for x,k in test_d:
            res = perimeter(x)
            self.assertEqual(res, k)