import math


def four_line_area(k1, c1, k2, c2, k3, c3, k4, c4):
    '''(number, number, number, number, number, number, number, number,)
     -> number
    Return point of intrasection of pair of non paralel lines and the area of
    shape

    >>> four_line_area(1.34, 10.18, 1.34 ,4.95, 13, 1, 4, 5)
    54.78
    '''
    if k1 != k2:
        return None

    per_t1 = line_intersection(k1, c1, k3, c3)
    per_t2 = line_intersection(k2, c2, k4, c4)
    per_t3 = line_intersection(k2, c2, k3, c3)
    per_t4 = line_intersection(k4, c4, k1, c1)

    a, b, h = find_h(per_t1, per_t2, per_t3, per_t4)

    return(area_trap(a, b, h))


def line_intersection(k1, c1, k2, c2):
    ''' (number, number, number, number) -> tuple(float, float)
    Return point of intrasection of pair of non paralel lines
    >>> line_intersection(3.89, 1.34, 0.78, 2.22)
    (0.28, 2.44)

    >>> line_intersection(3, 1, 10, 2)
    (-0.14, 0.57)
    '''
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


def find_h(per_t1, per_t2, per_t3, per_t4):
    '''(number, number, number, number) -> tuple(float, float, float)
    Return the height of trapeze
    '''
    x_t1, y_t1 = per_t1
    x_t2, y_t2 = per_t2

    x_triangle1 = x_t2
    y_triangle1 = y_t2

    a = distance(x_t1, y_t1, x_t2, y_t2)

    x_t1, y_t1 = per_t3
    x_t2, y_t2 = per_t4

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

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# four_line_area(1.34, 10.18, 1.34, 4.95, 13, 1, 4, 5)
print(four_line_area(1, 5, 1, 2, 3, 4, 3, 3))
