def egg_carton_box(eggs):
    ''' (number) -> list
    Return a number of boxes that you need to put all egss

    >>> egg_carton_box(12)
    [6, 6]

    >>> egg_carton_box(28)
    [10, 10, 10]

    >>> egg_carton_box(24)
    [4, 10, 10]
    '''
    lst_of_boxes = []

    if eggs > 0:
        if eggs in range(11, 13):
            for i in range(2):
                lst_of_boxes.append(6)
        else:
            for i in range(eggs // 10):
                lst_of_boxes.append(10)
            rem = eggs % 10
            if rem <= 4:
                lst_of_boxes.append(4)
            if rem in range(5, 7):
                lst_of_boxes.append(6)
            if rem >= 7:
                lst_of_boxes.append(10)

            return sorted(lst_of_boxes)
    else:
        return[]


print(egg_carton_box(0))
