import math
def area(r):
    if isinstance(r, str):
        return 'error'
    if isinstance(r, bool):
        return 'error'
    if r < 0:
        return 'error'
    if r == 0:
        return 'impossible to calculate area'
    return math.pi * r * r
'''Функция нахождения площади круга: принимает число r, возвращает произведение квадрата r и числа пи'''

def perimeter(r):
    if isinstance(r, str):
        return 'error'
    if isinstance(r, bool):
        return 'error'
    if r < 0:
        return 'error'
    if r == 0:
        return 'impossible to calculate perimeter'
    return 2 * math.pi * r
'''Функция нахождения периметра круга: возвращает удвоенное произведение числа пи и r'''