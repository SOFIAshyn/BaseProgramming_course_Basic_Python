def total_occurrences(s1, s2, ch):
    """ (str, str, str) -> int

    Precondition: len(ch) == 1
    Return the total number of times that ch occurs in s1 and s2.

    >>> total_occurrences('color', 'yellow', 'l')
    3

    >>> total_occurrences('red', 'blue', 'l')
    1

    >>> total_occurrences('green', 'purple', 'b')
    0
    """

    if len(ch) == 1:
        return (s1 + s2).count(ch)
    else:
        return 0

print(total_occurrences('green', 'purple', 'b'))
