def sieve_flavius(n):
    """(int) -> list

    Return the list of lucky numbers in range of inputed number

    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(0)
    []
    """
    lst = list(range(1, n+1))[::2]
    cursor = 0

    while cursor < len(lst) - 1:
        cursor += 1
        for i, val in enumerate(lst):
            if (i + 1) % lst[cursor] == 0:
                del lst[val]
        print(lst)
    return lst

    # lst = list(range(1, n+1))[::2]
    # cursor = 0
    #
    # while cursor < len(lst) - 1:
    #     cursor += 1
    #     new_lst = []
    #     for i, val in enumerate(lst):
    #         if (i + 1) % lst[cursor]:
    #             new_lst.append(val)
    #     lst = new_lst
    # return lst





if __name__ == "__main__":
    import doctest
    doctest.testmod()
#del [::2]
