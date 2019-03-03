import timeit
import random


def linear_search_while(lst, value):
    """
    (list, object) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> linear_search_while([2, 5, 1, -3], 5)
    1
    >>> linear_search_for([2, 5, 1, -3], 4)
    -1
    """
    i = 0  # The index of the next item in lst to examine.
    # Keep going until we reach the end of lst or until we find value.
    while i != len(lst) and lst[i] != value:
        i = i + 1
        # If we fell off the end of the list, we didn't find value.
        if i == len(lst):
            return -1
        else:
            return i


def linear_search_for(lst, value):
    """
    (list, object) -> int

    Return number of position of number

    >>> linear_search_for([2, 5, 1, -3], 5)
    1
    >>> linear_search_for([2, 4, 2], 2)
    0
    >>> linear_search_for([2, 5, 1, -3], 4)
    -1
    """
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def linear_search_pop(lst, value):
    """
    (list, object) -> int

    Return number of position of number

    >>> linear_search_pop([2, 5, 1, -3], 5)
    1
    >>> linear_search_pop([2, 4, 2], 2)
    0
    >>> linear_search_pop([2, 5, 1, -3], 4)
    -1
    """
    # Add the sentinel.
    lst.append(value)
    i = 0
    # Keep going until we find value.
    while lst[i] != value:
        i = i + 1
    # Remove the sentinel.
    lst.pop()
    # If we reached the end of the list we didn't find value.
    if i == len(lst):
        return -1
    else:
        return i


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    lst = [x for x in range(1, 10000)]
    val1 = 1
    val2 = 5000
    val3 = 10000

    file = open("search_time_test.txt", "w+")

    setup = [
        "from __main__ import linear_search_while",
        "from __main__ import linear_search_for",
        "from __main__ import linear_search_pop"
    ]

    functions_to_inv = [
        'linear_search_while({}, {})'.format(lst, val1),
        'linear_search_for({}, {})'.format(lst, val1),
        'linear_search_pop({}, {})'.format(lst, val1)
    ]

    for i in range(len(functions_to_inv)):
        time_lst = timeit.repeat(functions_to_inv[i], setup[i], \
                                 timeit.default_timer, 3, 10)

    for f_time in time_lst:
        file.write("If we are looking for the first\t {}". \
                   format(f_time) + '\n')

    functions_to_inv = [
        'linear_search_while({}, {})'.format(lst, val2),
        'linear_search_for({}, {})'.format(lst, val2),
        'linear_search_pop({}, {})'.format(lst, val2)
    ]

    for i in range(len(functions_to_inv)):
        time_lst = timeit.repeat(functions_to_inv[i], setup[i], \
                                 timeit.default_timer, 3, 10)

    for f_time in time_lst:
        file.write("If we are looking for middle\t {}".format(f_time) + '\n')

    functions_to_inv = [
        'linear_search_while({}, {})'.format(lst, val3),
        'linear_search_for({}, {})'.format(lst, val3),
        'linear_search_pop({}, {})'.format(lst, val3)
    ]

    for i in range(len(functions_to_inv)):
        time_lst = timeit.repeat(functions_to_inv[i], setup[i], \
                                 timeit.default_timer, 3, 10)

    for f_time in time_lst:
        file.write("If we are looking for end\t {}".format(f_time) + '\n')
