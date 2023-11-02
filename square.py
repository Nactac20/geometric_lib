import unittest
def area(a):
    return a * a
'''Функция нахождения плошади квадрата: принимает число a, возвращает квадрат числа a'''

def perimeter(a):
    return 4 * a
'''Функция нахождения периметра квадрата: принимает число a, возвращает произведение a и 4'''
class TestSquareCase(unittest.TestCase):
    def area_test_0(self):
        res = area(0)
        self.assertEqual(res, 0)
    def area_test_1(self):
        res = area(1)
        self.assertEqual(res, 1)
    def perimeter_test_0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def perimeter_test_1(self):
        res = perimeter(1)
        self.assertEqual(res, 4)