import unittest
def area(a, h):
    return a * h / 2
'''Функция нахождения плошади треугольника: принимает число a - сторонa треугольника, и c - угол между этими сторонами, возвращает половину произведения a и h'''
def perimeter(a, b, c): 
    return a + b + c 
'''Функция нахождения периметра треугольника: принимает числа a, b, c - стороны треугольника, возвращает сумму a, b, c'''
class TestTriangleCase(unittest.TestCase):
    def area_test_0(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def area_test_1(self):
        res = area(1, 1)
        self.assertEqual(res, 0.5)

    def perimeter_test_0(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def perimeter_test_1(self):
        res = perimeter(1, 2, 2)
        self.assertEqual(res, 5)