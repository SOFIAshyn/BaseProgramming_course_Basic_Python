import math


def four_line_area(k1, c1, k2, c2, k3, c3, k4, c4):
    '''(number, number, number, number, number, number, number, number,)
     -> number
    Return area of shape

    >>> four_line_area(2, 5, 2, 2, 7, 4, 5, 3)
    0.67

    >>> four_line_area(1, 5, 1, 2, 3, 4, 3, 3)
    1.64

    >>> four_line_area(10, 5, 10, 2, 5, 2, 7, 4)
    1.39
    '''
    if k1 != k2:
        return None

    per1 = line_intersection(k1, c1, k3, c3)
    per2 = line_intersection(k3, c3, k2, c2)
    per3 = line_intersection(k2, c2, k4, c4)
    per4 = line_intersection(k4, c4, k1, c1)

    x1, y1 = per1
    x2, y2 = per2
    a = distance(x1, y1, x2, y2)
    x1, y1 = per2
    x2, y2 = per3
    b = distance(x1, y1, x2, y2)
    x1, y1 = per3
    x2, y2 = per4
    c = distance(x1, y1, x2, y2)
    x1, y1 = per4
    x2, y2 = per1
    d = distance(x1, y1, x2, y2)
    x1, y1 = per1
    x2, y2 = per3
    f1 = distance(x1, y1, x2, y2)
    x1, y1 = per2
    x2, y2 = per4
    f2 = distance(x1, y1, x2, y2)

    return (quadrangle_area(a, b, c, d, f1, f2))


def line_intersection(k1, c1, k2, c2):
    ''' (number, number, number, number) -> tuple(float, float)
    Return point of intrasection of pair of non paralel lines
    >>> line_intersection(3.89, 1.34, 0.78, 2.22)
    (0.28, 2.44)

    >>> line_intersection(3, 1, 10, 2)
    (-0.14, 0.57)
    '''
    if k1 == k2:
        return None
    y = round((c2 * k1 - c1 * k2)/(k1 - k2), 2)
    x = round(((y - c1)/k1), 2)
    return (x, y)


def distance(x1, y1, x2, y2):
    '''(number, number, number, number) -> float
    Distance between two coordinates
    >>> distance(3, 1, 10, 2)
    7.07

    >>> distance(3.89, 1.34, 0.78, 2.22)
    3.23
    '''
    dist = round((((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)), 2)
    return dist


def quadrangle_area(a, b, c, d, f1, f2):
    '''(number, number, number, number, number, number) -> float
    Return the area of the shape
    >>> quadrangle_area(10.34, 10.17, 10.16 ,4.95, 13, 11.88)
    74.43

    >>> quadrangle_area(3, 1, 10 , 4, 3, 2)
    None
    '''
    t = 4 * f1**2 * f2**2 - (b**2 + d**2 - a**2 - c**2)**2
    if t > 0:
        s_area = round(t ** (0.5) / 4, 2)
        return (s_area)
    else:
        return None

#print(four_line_area(10, 5, 10, 2, 5, 2, 7, 4))
print(four_line_area(1, 5, 1, 2, 3, 4, 3, 3))
