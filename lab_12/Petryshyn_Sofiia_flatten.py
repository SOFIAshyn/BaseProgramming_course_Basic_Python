def flatten(lst):
    """
    (list) -> list

    Return list without inside lists

    >>> flatten([1,[2]])
    [1, 2]
    """
    new_lst = []
    if isinstance(lst, list):
        for el in lst:
            if isinstance(el, list):
                new_lst.extend(flatten(el))
            else:
                new_lst.append(el)
        return new_lst
    else:
        return lst


if __name__ == "__main__":
    import doctest

    doctest.testmod()
