import unittest
def area(a, b):
    return a * b 
'''Функция нахождения площади прямоугольника: принимает два числа a и b, возвращает произведение a и b'''
def perimeter(a, b):
    return 2*(a+b)
'''Функция нахождения периметра прямоугольника: принимает два числа a, b, возвращает сумму произведений чисел a и 2, b и 2'''
class TestRectangleCase(unittest.TestCase):
    def area_test_0(self):
        res = area(0, 10)
        self.assertEqual(res, 0)
    def area_test_1(self):
        res = area(1, 1)
        self.assertEqual(res, 1)
    def perimeter_test_0(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    def perimeter_test_1(self):
        res = perimeter(100, 100)
        self.assertEqual(res, 400)