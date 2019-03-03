def equal_parts(numbers):
    ''''list(int) -> (list(int),list(int))

    Return two integers list of equal sum as an attempt at a partition of
input numbers

    >>> equal_parts([2, 4, 5, 6, 7, 12, 13, 23, 1, 1, 34])
    ([23, 13, 7, 6, 4, 1], [34, 12, 5, 2, 1])
    >>> equal_parts([-2, 4, -5, 6, 7, 12, -13, 23, 1, 1, 34, 34, 12, 1,\
 67, 34, 98])
    ([67, 34, 34, 12, 12, 6, 1, 1], [98, 34, 23, 7, 4, 1, -2, -5, -13])
    '''

    l1 = []
    l2 = []
    numbers.sort(reverse = True)

    for i in numbers:
        if sum(l1) < sum(l2):
            l1.append(i)
        else:
            l2.append(i)
    return l1, l2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
