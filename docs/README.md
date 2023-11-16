# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a*b*sin(ab))/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Общее описание решения
В проекте *Geometric_lib* представлены различные математический формулы для вычисления периметра и площади следующих геометрических фигур:
* Круг
* Прямоугольник
* Квадрат
* Треугольник

Данный проект при помощи языка программирования **Python** позволяет при определенных входных данных пользователя вычислить площадь или периметр соответствующих фигур.

## Описание работы функций файла *circle.py*
* **area(r)** - Функция нахождения площади круга: принимает число r, возвращает произведение квадрата r и числа пи. Пример вызова функции: **print(area(2))** ==> **12.566370614359172**
* **perimeter(r)** - Функция нахождения периметра круга: возвращает удвоенное произведение числа пи и r. Пример вызова функции: **print(perimeter(3))** ==> **18.84955592153876**

## Описание работы функций файла *rectangle.py*
* **area(a, b)** - Функция нахождения площади прямоугольника: принимает два числа a и b, возвращает произведение a и b. Пример вызова функции: **print(area(2, 3))** ==> **6**
* **perimeter(a, b)** - Функция нахождения периметра прямоугольника: принимает два числа a, b, возвращает сумму произведений чисел a и 2, b и 2. Пример вызова функции: **print(perimeter(2, 3))** ==> **10**

## Описание работы функций файла *square.py*
* **area(a)** - Функция нахождения плошади квадрата: принимает число a, возвращает квадрат числа a. Пример вызова функции: **print(area(2))** ==> **4**
* **perimeter(a)** - Функция нахождения периметра квадрата: принимает число a, возвращает произведение a и 4. Пример вызова функции: **print(perimeter(2))** ==> **8**

## Описание работы функций файла *triangle.py*
* **area(a, b, c)** - Функция нахождения плошади треугольника: принимает числа a, b - стороны треугольника, и c - угол между этими сторонами, возвращает половину произведения a, b и синуса угла c. Пример вызова функции: **print(area(2, 4, 30))** ==> **2**
* **perimeter(a, b, c)** - Функция нахождения периметра треугольника: принимает числа a, b, c - стороны треугольника, возвращает сумму a, b, c. Пример вызова функции: **print(perimeter(2, 3, 4))** ==> **9**

## История изменения проекта (обновленная версия)
C:\Users\Анастасия\Desktop\geometric_lib>git log
commit e65c087d086af039ba306e8b259ea626b2ced6c1 (HEAD -> unittest)
Author: Nactac20 <nactac20@gmail.com>
Date:   Fri Nov 17 02:36:22 2023 +0300

    Добавлены unittests для файлов

commit 2d0b4a1021c51af0de16ff1e7577536fd8a6c87c
Author: Nactac20 <nactac20@gmail.com>
Date:   Fri Nov 17 02:30:09 2023 +0300

    Добавлена модификации файлов
commit 9f8bd933a5fffe5a780d5711a90327feead468d4 (HEAD -> new_doc)
Author: Nactac20 <nactac20@gmail.com>
Date:   Thu Oct 5 22:39:27 2023 +0300

    Добавлена документация для файла triangle.py

commit 851cc476df716fb0e0ad945cbc8fb3500f542974
Author: Nactac20 <nactac20@gmail.com>
Date:   Thu Oct 5 22:17:02 2023 +0300

    Добавлена документация для файла square.py

commit bb508a4468af8b00f85fe0509ae0ce3fb5712655
Author: Nactac20 <nactac20@gmail.com>
Date:   Thu Oct 5 22:15:04 2023 +0300

    Добавлена документация для файла rectangle.py

commit 136d9c5998e6a653a555a4b2586ee2158841faa9
Author: Nactac20 <nactac20@gmail.com>
Date:   Thu Oct 5 22:14:12 2023 +0300

    Добавлена документация для файла circle.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added
# Создание unittests
Тесты создавались с целью протестировать программы и их функции. 
Все тесты проверяют корректность работы программ при вводе валидового, нулевого, отрицательного, строкового, булевого значений
# Результаты unittests
## circle.py
| Радиус a | Площадь (ожидаемый результат) | Периметр (ожидаемый результат)    | Площадь (фактический результат) | Периметр (фактический результат)|
|------|-------------------------------|-----------------------------------|---------------------------------|----------------|
| 3    | 9π                            | 6π                                | 9π                              |6π|
| -2   | error                         | error                             | error                           |error|
| 2.5  | 6.25π                         | 5π                                | 6.25π                           |5π|
| 0    | impossible to calculate area  | impossible to calculate perimeter | impossible to calculate area    |impossible to calculate perimeter|
| True | error                         | error                             | error                           |error|
| fgd  | error                         | error                             | error                           |error|

## rectangle.py
| Сторона a | Сторона b | Площадь (ожидаемый результат) | Площадь (фактический результат)|
|-----------|----------|-------------------------------|---------------------------|
| 3         | 4        | 12                            |12|
| -2        | 0        | impossible to calculate area  |impossible to calculate area|
| 2.5       | 6.25     | 15.625                        |15.625|
| 0         | 0        | impossible to calculate area  |impossible to calculate area|
| -2.5      | -1       | error                         |error|
| True      | -1       | error                         |error|
| 'fgd'     | 1        | error                         |error|

| Сторона a | Сторона b | Периметр (ожидаемый результат) | Периметр (фактический результат)  |
|-----------|----------|--------------------------------|-----------------------------------|
| 1         | 4        | 10                             | 10                                |
| -10       | 6        | error                          | error                             |
| 3.5       | 12       | 31                             | 31                                |
| 0         | 0        | impossible to calculate perimeter| impossible to calculate perimeter |
| -2.5      | -4       | error                          | error                             |
| True      | -1       | error                          | error                             |
| 'fgd'      | 1        | error                          | error                             |

## square.py
| Сторона a | Площадь (ожидаемый результат) | Периметр (ожидаемый результат)    |Площадь (фактический результат) | Периметр (фактический результат) |
|-----------|-------------------------------|-----------------------------------|-------------------------------------------------|-----------------|
| 3         | 9                             | 12                                |9|12|
| -2        | error                         | error                             |error|error|
| 2.5       | 6.25                          | 10                                |6.25|10|
| 0         | impossible to calculate area  | impossible to calculate perimeter |impossible to calculate area|impossible to calculate perimeter|
| True      | error                         | error                             |error|error|
| 'fgd'      | error                         | error                             |error|error|
## triangle.py
| Сторона a | Высота h | Площадь (ожидаемый результат) | Площадь (фактический результат)|
|-----------|---|-------------------------------|------------------|
| 1         | 3 | 1.5                             |1.5|
| -2        | 0 | impossible to calculate area| impossible to calculate area |
| 3.5       |4|7|7|
|0|2.5|impossible to calculate area|impossible to calculate area |
|-2.5|-6|error|error|
|0|0|impossible to calculate area |impossible to calculate area |
|True|1|error|error|
|'fgd'|-2|error|error|


| Сторона a | Сторона b | Сторона c| Периметр (ожидаемый результат) | Периметр (фактический результат)|
|-----------|-----------|---|--------------------------------|----------------|
| 1         | 3         | 5 | not triangle | not riangle|
| -10         | 0         | 5.4 | impossible to calculate perimeter  |impossible to calculate perimeter|
|0| 0         |0|impossible to calculate perimeter|impossible to calculate perimeter|
|3| 5         |2|10|10|
|2.5| 3.5       |6|12|12|
|True| 1         |-1|error|error|
|'fgd'| 8         |-9|error|error|