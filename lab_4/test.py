# def my_alg(a, b, c = 1):
#     """Function for my algorithm
#     """
#     # TODO: ghghk
#     return a * b * c
#
# def my_alg_div(a = 8, b = 9, c = 1):
#     """Function for my algorithm
#     """
#     # TODO: ghghk
#     return a * b / c
#
# def f(*args, **kwargs):
#     # arguments, key arguments
#     print(type(args), args)
#     print(type(kwargs), kwargs)
#
# def func(**kwargs):
#     keys = {"a", "b", "c"}
#     for key, value in kwargs:
#         print(f"key {k}: value {v}". format(k = key, v  = value))
#
# if (__name__ == "__main__"):
#     print(f(1, 5, 3, 4))
#     print(f(1, 5, 3, 4, 6))
#     print(f(1, 5, 3, 4, z = 7, c = 8))
#
#     # my_alg(2, my_alg_div())
#     # func(a = 1, b = 5)
# #    print(globals())
#     import doctest
#     doctest.testmod()

# eight_p = [('яловичина', 700), ('буряк', 500), ('картопля', 500), \
# ('морква', 200), ('цибуля', 200), ('помідори', 300), ('капуста', 300)]
# #
# # for ing in eight_p:
# #     ing = ing[:1] + ((ing[1] * (16 // 8)),) + ing[2:]
# #     print (ing)
#
# pos = 0
# eight_new = []
# for ingrtedient in eight_p:
#     #rest_portions = portions % 8
#     ingrtedient = ingrtedient[:1] + ((ingrtedient[1] * (33 // 8)),) + ingrtedient[2:]
#     print(type(ingrtedient))
#     eight_new.insert(pos, ingrtedient)
#     pos += 1
#
# print(eight_new)


# rest_portions = portions % 8
# for ingredient in eight_p:
#     ingredient = ingredient[:1] + ((ingredient[1] * (portions // 8)),) + ingredient[2:]
#
# for j in range(rest_portions // 2):
#     for ingredient2 in eight_p:
#         ingredient2 = ingredient[:1] + ((ingredient[1] + round(i[1] // 4, -2)),) + i[1:]
#
# rest_portions %= 2
# for ingredient3 in range(rest_portions):

# print ("yes" if 4 % 2 != 0 else "no")
#
# eight_p = [('яловичина', 700), ('буряк', 500), ('картопля', 500), \
# ('морква', 200), ('цибуля', 200), ('помідори', 300), ('капуста', 300)]
#
# def borsch_ingredients(portions):
#     '''(int) -> tuple
#     Function
#
#     >>> borsch_ingredients(8)
#     [('яловичина', 700 ), ('буряк', 500), ('картопля', 500), ('морква', 200),
#      ('цибуля', 200), ('помідори', 300), ('капуста', 300)]
#
#     >>> borsch_ingredients(10)
#     [('яловичина', 900), ('буряк', 700), ('картопля', 700), ('морква', 300),
#      ('цибуля', 300), ('помідори', 400), ('капуста', 400)]
#     '''
#
#     eight_p_ = []
#     pos = 0
#     for ingredient in eight_p:
#         check = (ingredient[1] // 8) * portions // 100
#         ingredient = ingredient[:1] + \
#         ((((check + 1) * 100),) \
#         if (check % 100 != 0) else \
#         ((check * 100),))
#         eight_p_.insert(pos, ingredient)
#         pos += 1
#     return eight_p_
#
# print(borsch_ingredients(10))

# def set_up_rating(name, rating):
#     name = 'Arman'
#     rating.append(100)
#     rating = 49
#     #return name, rating
#
# n = ''
# r = []
# set_up_rating(n, r)
#
# print(n, r)

#****************************
# assert
#****************************
# def f(num):
#     assert isinstance(num, int)
#     return (num // 2)
#
# print(f(78))

# passed = True
# assert passed, 'Not passed'


# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# func(2, 5, 6, 7, 8, n = 0, m = 0, k = "gjnhmh")

###########ASSERT#########################################
# def onesDigit(n):
#     return n % 10
#
# def testOnesDigit():
#     print("Testing onesDigit()...", end="")
#     assert(onesDigit(5) == 5)
#     assert(onesDigit(123) == 3)
#     assert(onesDigit(100) == 0)
#     assert(onesDigit(999) == 9)
#     #assert(onesDigit(-123) == 3) # Буде викликати AssertionError
#     print("Passed!")
# testOnesDigit()
###########ASSERT#########################################

# def line_intersection(k1, c1, k2, c2):
#     ''' (number, number, number, number) -> tuple(float, float)
#     знаходження точки перетину двох прямих.
#     '''
#     if k1 != k2:
#         return None
#     try:
#         y = round((c2 * k1 - c1 * k2)/(k1 - k2), 2)
#         x = round(((y - c1)/k1), 2)
#         return (x, y)
#     except (ZeroDivisionError):
#         return None
#
# print(line_intersection(3, 4, 3, -10))

# def quadrangle_area(a, b, c, d, f1, f2):
#     '''(number, number, number, number, number, number) -> float
#     Return the area of the shape
#     >>> quadrangle_area(10.34, 10.17, 10.16 ,4.95, 13, 11.88)
#     74.43
#
#     >>> quadrangle_area(3, 1, 10 , 4, 3, 2)
#     None
#     '''
#     t = 4 * f1**2 * f2**2 - (b**2 + d**2 - a**2 - c**2)**2
#     if t > 0:
#         s_area = round(t ** (0.5) / 4, 2)
#         return (s_area)
#     else:
#         return None
#
# print(quadrangle_area(3, 1, 10 , 4, 3, 2))
#
# def distance(x1, y1, x2, y2):
#     '''(number, number, number, number) -> float
#     Distance between two coordinates
#     >>> distance(3, 1, 10, 2)
#     7.07
#
#     >>> distance(3.89, 1.34, 0.78, 2.22)
#     3.23
#     '''
#     dist = round((((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)), 2)
#     return dist
#
# print(distance(3.89, 1.34, 0.78, 2.22))


# def line_intersection(k1, c1, k2, c2):
#     ''' (number, number, number, number) -> tuple(float, float)
#     Return point of intrasection of pair of non paralel lines
#     >>> line_intersection(3.89, 1.34, 0.78, 2.22)
#     (0.28, 2.44)
#
#     >>> line_intersection(3, 1, 10, 2)
#     (-0.14, 0.57)
#     '''
#     if k1 == k2:
#         return None
#     y = round((c2 * k1 - c1 * k2)/(k1 - k2), 2)
#     x = round(((y - c1)/k1), 2)
#     return (x, y)
#
# print(line_intersection(3, 1, 10, 2))
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

if __name__ == "__main__":
    print(quadrangle_area(10.34, 1.17, 10.16 ,4.95, 13, 11.88))
    # import doctest
    # doctest.testmod()

# import math
#
# def f():
#     return (4, 6)
#
# a, b = f()
# print(a)
# print(b)
# print(round(math.radians(120), 2))
# print(round(math.atan(round(math.radians(30), 2)), 2))
# print(round(math.atan(math.radians(30)), 2))
