def egg_carton_box(eggs):
    '''(int) -> int
    Function for searching a min number of boxes to put all eggs.

    >>> egg_carton_box(12)
    2
    >>> egg_carton_box(28)
    3
    '''
    if eggs % 10 == 0:
        num_box = eggs // 10
    else:
        num_box = eggs // 10 + 1
    return num_box

print(egg_carton_box(0))
