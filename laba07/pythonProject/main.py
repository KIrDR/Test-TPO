import math

def is_triangle(side1, side2, side3):
    """
    Проверяет, можно ли из трех заданных сторон создать треугольник.
    Возвращает True, если треугольник можно построить, и False в противном случае.
    """
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        return True
    else:
        return False

def perimeter(side1, side2, side3):
    """
    Вычисляет периметр треугольника.
    """
    if not is_triangle(side1, side2, side3):
        return -1
    return side1 + side2 + side3

def area(side1, side2, side3):
    """
    Вычисляет площадь треугольника по формуле Герона.
    """
    if not is_triangle(side1, side2, side3):
        return -1
    p = perimeter(side1, side2, side3) / 2
    return math.sqrt(p * (p - side1) * (p - side2) * (p - side3))

def inradius(side1, side2, side3):
    """
    Вычисляет радиус вписанной окружности треугольника.
    """
    if not is_triangle(side1, side2, side3):
        return -1
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return -2
    return area(side1, side2, side3) / (perimeter(side1, side2, side3) / 2)

def circumradius(side1, side2, side3):
    """
    Вычисляет радиус описанной окружности треугольника.
    """
    if not is_triangle(side1, side2, side3):
        return -1
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return -2
    return (side1 * side2 * side3) / (4 * area(side1, side2, side3))

#side1 = float(input("Введите длину первой стороны треугольника: "))
#side2 = float(input("Введите длину второй стороны треугольника: "))
#side3 = float(input("Введите длину третьей стороны треугольника: "))

#if is_triangle(side1, side2, side3):
#    print("Из этих сторон можно построить треугольник.")
#    print("Его периметр: ", perimeter(side1, side2, side3))
#    print("Его площадь: ", area(side1, side2, side3))
#    print("Радиус вписанной окружности: ", inradius(side1, side2, side3))
#    print("Радиус описанной окружности: ", circumradius(side1, side2, side3))
#else:
#    print("Из этих сторон нельзя построить треугольник.")
