def area(a):
    if isinstance(a, str):
        return 'error'
    if isinstance(a, bool):
        return 'error'
    if a == 0:
        return 'impossible to calculate area'
    if a < 0:
        return 'error'
    return a * a
'''Функция нахождения плошади квадрата: принимает число a, возвращает квадрат числа a'''
def perimeter(a):
    if isinstance(a, str):
        return 'error'
    if isinstance(a, bool):
        return 'error'
    if a == 0:
        return 'impossible to calculate perimeter'
    if a < 0:
        return 'error'
    return 4 * a
'''Функция нахождения периметра квадрата: принимает число a, возвращает произведение a и 4'''
