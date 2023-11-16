def area(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return 'error'
    if isinstance(a, bool) or isinstance(b, bool):
        return 'error'
    if a == 0 or b == 0:
        return 'impossible to calculate area'
    if a < 0 or b < 0:
        return 'error'
    return a * b
'''Функция нахождения площади прямоугольника: принимает два числа a и b, возвращает произведение a и b'''
def perimeter(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return 'error'
    if isinstance(a, bool) or isinstance(b, bool):
        return 'error'
    if a == 0 or b == 0:
        return 'impossible to calculate perimeter'
    if a < 0 or b < 0:
        return 'error'
    if a == 0 or b == 0:
        return 'impossible to calculate perimeter'
    return 2*(a + b)
'''Функция нахождения периметра прямоугольника: принимает два числа a, b, возвращает сумму произведений чисел a и 2, b и 2'''