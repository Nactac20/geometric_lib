import unittest
from circle import*
class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
       test_d = ((3,9*math.pi), (-2,'error'), (2.5,6.25*math.pi), (0,'impossible to calculate area'), (True,'error'), ('fgd','error'))
       for x,k in test_d:
          res = area(x)
          self.assertEqual(res, k)
    def test_circle_perimeter(self):
        test_d = ((3,6*math.pi), (-2,'error'), (2.5,5*math.pi),(0,'impossible to calculate perimeter'), (True,'error'), ('fgd','error'))
        for x,k in test_d:
            res = perimeter(x)
            self.assertEqual(res, k)