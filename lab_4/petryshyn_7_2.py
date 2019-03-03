import math


def four_line_area(k1, c1, k2, c2, k3, c3, k4, c4):
    '''(number, number, number, number, number, number, number, number,)
     -> number
    Return area of quadrangle

    >>> four_line_area(0.1, 1, 9, 3, 6, 1, 16, 5)
    0.43

    >>> print(four_line_area(1, 5, 1, 2, 3, 4, 3, 3))
    23.75

    >>> four_line_area(1.34, 10.18, 1.34, 4.95, 13, 1, 4, 5)
    51.58
    '''

    per1 = line_intersection(k1, c1, k3, c3)
    per2 = line_intersection(k3, c3, k2, c2)
    per3 = line_intersection(k2, c2, k4, c4)
    per4 = line_intersection(k4, c4, k1, c1)

    if k1 == k2:
        a, b, h = find_h(per1, per2, per3, per4)

        return(area_trap(a, b, h))

    else:
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

        type_sq, in_circle = corners(k1, k2, k3, k4)

        if type_sq == 1:
                if in_circle == 1:
                    return (area_of_Brah(a, b, c, d))
                else:
                    x1, y1 = per1
                    x2, y2 = per3
                    f1 = distance(x1, y1, x2, y2)
                    x1, y1 = per2
                    x2, y2 = per4
                    f2 = distance(x1, y1, x2, y2)

                    return quadrangle_area(a, b, c, d, f1, f2)
        else:
            x1, y1 = per1
            x2, y2 = per3
            diagonal = distance(x1, y1, x2, y2)

            tr_s1, tr_s2 = triangles_area(a, b, c, d, diagonal)
            area_notconvex_quad = tr_1 + tr_2

            return area_notconvex_quad


def line_intersection(k1, c1, k2, c2):
    ''' (number, number, number, number) -> tuple(float, float)
    Return point of intrasection of pair of non paralel lines

    >>> line_intersection(3.89, 1.34, 0.78, 2.22)
    (0.28, 2.44)

    >>> line_intersection(3, 1, 10, 2)
    (-0.14, 0.57)
    '''
    try:
        y = round((c2 * k1 - c1 * k2)/(k1 - k2), 2)
        x = round(((y - c1)/k1), 2)
        return (x, y)
    except (ZeroDivisionError):
        print("Error")
        return None


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


def find_h(per1, per2, per3, per4):
    '''(number, number, number, number) -> tuple(float, float, float)
    Return the height of trapeze
    '''
    x_t1, y_t1 = per1
    x_t2, y_t2 = per2

    x_triangle1 = x_t2
    y_triangle1 = y_t2

    a = distance(x_t1, y_t1, x_t2, y_t2)

    x_t1, y_t1 = per3
    x_t2, y_t2 = per4

    x_triangle2 = x_t2
    y_triangle2 = y_t2

    b = distance(x_t1, y_t1, x_t2, y_t2)
    c1 = distance(x_triangle1, y_triangle1, x_triangle2, y_triangle2)
    c2 = round(abs(x_triangle2 - x_triangle1), 2)

    h = round(math.sqrt(c1 ** 2 - c2 ** 2), 2)
    return (a, b, h)


def area_trap(a, b, h):
    '''(number, number, number) -> float
    Return the area of the shape
    '''
    s_trap = round(((a + b) / 2 * h), 2)
    if s_trap < 0:
        return None
    return s_trap


def tan_to_deg(a):
    return round(math.atan(round(math.radians(a), 2)), 2)


def corners(k1, k2, k3, k4):
    '''(number, number, number) -> tuple(number, number)
    Return if the quadrange is convex or no
    and if it is convex return if it is inserts in circle or no
    '''
    in_circle = 0

    cor1 = k1 - k4
    cor2 = k3 - k2
    cor3 = k2 - k4
    cor4 = k4 - k1

    sum_cor = cor1 + cor2 + cor3 + cor4

    if tan_to_deg(sum_cor) <= 180:
        # convex
        type_sq = 1
    else:
        # not convex
        type_sq = 0

    if type_sq == 0:
        if tan_to_deg(cor1 + cor3) == 180:
            # insert
            in_circle = 1
        else:
            # can't be insert
            in_circle = 0

    return (type_sq, in_circle)


def quadrangle_area(a, b, c, d, f1, f2):
    '''(number, number, number, number, number, number) -> float
    Return the area of the shape

    >>> quadrangle_area(10.34, 10.17, 10.16 ,4.95, 13, 11.88)
    74.43

    >>> quadrangle_area(10.34, 1.17, 10.16 ,4.95, 13, 11.88)
    61.97
    '''
    t = 4 * f1**2 * f2**2 - (b**2 + d**2 - a**2 - c**2)**2
    if t > 0:
        s_area = round(t ** (0.5) / 4, 2)
        return (s_area)
    else:
        return None


def area_of_Brah(a, b, c, d):
    '''(number, number, number, number) -> number
    Return area of inserted in circle quadrange
    '''
    p = round((a + b + c + d) / 2, 2)
    expression = (p - a) * (p - b) * (p - c) * (p - d)
    if expression > 0:
        s_area = round(math.sqrt(expression), 2)
        return (s_area)
    else:
        return None


def quadrangle_notconvex_area(a, b, c, d, diagonal):
    '''(number, number, number, number, number) -> tuple(number, number)
    Return area of 2 triangles to find out an area of
    not convex aquadrangle
    '''
    p1 = a + b + diagonal
    p2 = c + d + diagonal

    expression1 = (p - a) * (p - b) * (p - diagonal)
    expression1 = (p - c) * (p - d) * (p - diagonal)
    if expression1 > 0 and expression2 > 0:
        tr_s1 = round(math.sqrt(expression1), 2)
        tr_s2 = round(math.sqrt(expression2), 2)
        return tr_s1, tr_s2
    else:
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(four_line_area(1.34, 10.18, 1.34, 4.95, 13, 1, 4, 5))
