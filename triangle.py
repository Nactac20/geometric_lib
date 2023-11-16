def area(a, h):
    if isinstance(a, str) or isinstance(h, str):
        return 'error'
    if isinstance(a, bool) or isinstance(h, bool):
        return 'error'
    if a == 0 or h == 0:
        return 'impossible to calculate area'
    if a < 0 or h < 0:
        return 'error'
    return a * h / 2
'''Функция нахождения плошади треугольника: принимает число a - сторонa треугольника, и c - угол между этими сторонами, возвращает половину произведения a и h'''
def perimeter(a, b, c):
    if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
        return 'error'
    if isinstance(a, bool) or isinstance(b, bool) or isinstance(c, bool):
        return 'error'
    if a == 0 or b == 0 or c == 0:
        return 'impossible to calculate perimeter'
    if a + b >= c and b + c >= a and a + c >= b:
        return a + b + c
    return 'not triangle'
    if a < 0 and b < 0 and c < 0:
        return 'error'
    return a + b + c
'''Функция нахождения периметра треугольника: принимает числа a, b, c - стороны треугольника, возвращает сумму a, b, c'''