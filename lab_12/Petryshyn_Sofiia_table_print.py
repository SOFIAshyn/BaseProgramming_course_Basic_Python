def rec_count(lst, i, j):
    """
    (list, int, int) -> list

    Return list of counted numbers

    >>> rec_count([[0] * 4 for i in range(5)], 4, 0)
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
    """
    if j < len(lst[0]):
        if i == 0 or j == 0:
            lst[i][j] = 1
        else:
            lst[i][j] = lst[i - 1][j] + lst[i][j - 1]
        return rec_count(lst, i, j + 1)
    else:
        return lst


def rec_print(lst, i, j):
    """
    (list, int, int) -> list

    Return list of counted numbers

    >>> rec_print([[0] * 4 for i in range(5)], 0, 0)
    0    0    0    0    [[0, 0, 0, 0], [0, 0, 0, 0], \
[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    if j < len(lst[0]):
        print("{:<5}".format(lst[i][j]), end="")
        return rec_print(lst, i, j + 1)
    else:
        return lst


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    n, m = list(map(int, (input \
                              ("Print two numbers for table(lenght, width): " \
                               ).split())))
    table = [[0] * m for i in range(n)]

    # Investigation of recoursy
    for i in range(len(table)):
        table = rec_count(table, i, 0)

    for i in range(len(table)):
        table = rec_print(table, i, 0)
        print('\n')
