# eight_p = [('яловичина', 700), ('буряк', 500), ('картопля', 500), \
# ('морква', 200), ('цибуля', 200), ('помідори', 300), ('капуста', 300)]
#
# def borsch_ingredients(portions):
#     '''(int) -> tuple
#     Function gives you numbers of grams of each ingredient of borsch
#     for number of people that you give for function
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
#     eight_p_new = []
#     pos = 0
#     for ingredient in eight_p:
#         if portions % 8 == 0:
#             ingredient = ingredient[:1] + ((ingredient[1] * (portions // 8)),)
#         else:
#             ingredient = ingredient[:1] + (((((ingredient[1] // 8) * portions) // 100 + 1) * 100) if portions % 100 != 0 else ((ingredient[1] // 8) * portions),)
#         eight_p_new.insert(pos, ingredient)
#         pos += 1
#     return eight_p_new
#
# print(borsch_ingredients(16))

eight_p = [
    ('яловичина', 700), ('буряк', 500), ('картопля', 500),
    ('морква', 200), ('цибуля', 200), ('помідори', 300), ('капуста', 300)]

def borsch_ingredients(portions):
    '''(int) -> list
    Function gives you numbers of grams of each ingredient of borsch
    for number of people that you give for function

    >>> borsch_ingredients(8)
    [('яловичина', 700 ), ('буряк', 500), ('картопля', 500), ('морква', 200),
     ('цибуля', 200), ('помідори', 300), ('капуста', 300)]

    >>> borsch_ingredients(10)
    [('яловичина', 900), ('буряк', 700), ('картопля', 700), ('морква', 300),
     ('цибуля', 300), ('помідори', 400), ('капуста', 400)]
    '''

    eight_p_new = []
    pos = 0
    for ingredient in eight_p:
        if portions % 8 == 0:
            ingredient = ingredient[:1] + ((ingredient[1] * (portions // 8)),)
        else:
            ingredient = ingredient[:1] + (((((ingredient[1] // 8) * portions) // 100 + 1) * 100) if (portions % 100 != 0) else ((ingredient[1] // 8) * portions), )
        eight_p_new.insert(pos, ingredient)
        pos += 1
    return eight_p_new
