def happy_number(num):
    """(int) -> bool

    Return True is the number is happy and False in another case
    num: an integer > 0

    >>> happy_number(12345)
    False
    >>> happy_number(43211234)
    True
    >>> happy_number(191234)
    True
    """
    assert(num > 0), "AssetationError"
    num = ((8 - len(str(num))) * "0" + str(num))

    int_lst = [int(i) for i in num]
    return (sum(int_lst[:4]) == sum(int_lst[4:]))


def count_happy_numbers(n):
    """(int) -> int

    Return the number of happy numbers that are in the range of n

    >>> count_happy_numbers(20002)
    5
    >>> count_happy_numbers(120003)
    729
    """
    all_happy = 0
    if len(str(n)) > 4:
        for i in range(1, n + 1):
            if happy_number(i) is True:
                all_happy += 1
    return all_happy


def happy_numbers(m, n):
    """(int, int) -> list

    Return all happy numbers from range m to n
    
    >>> happy_numbers(100, 20002)
    [10001, 10010, 10100, 11000, 20002]
    >>> happy_numbers(20002, 29002)
    [20002, 20011, 20020, 20101, 20110, 20200, 21001, 21010, 21100, 22000]
    """
    lst_of_happy_in_range = []
    lst_of_happy_in_range = [int(i) for i in range(m, n + 1)
                            if happy_number(i) == True]
    return lst_of_happy_in_range
