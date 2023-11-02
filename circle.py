import math
import unittest

def area(r):
    return math.pi * r * r
'''Функция нахождения площади круга: принимает число r, возвращает произведение квадрата r и числа пи'''

def perimeter(r):
    return 2 * math.pi * r
'''Функция нахождения периметра круга: возвращает удвоенное произведение числа пи и r'''
class TestCircleCase(unittest.TestCase):
    def area_test_0(self):
        res = area(0)
        self.assertEqual(res, 0)
    def area_test_1(self):
        res = area(1)
        self.assertEqual(res, math.pi)
    def perimeter_test_0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def perimeter_test_1(self):
        res = perimeter(1)
        self.assertEqual(res, 2 * math.pi)