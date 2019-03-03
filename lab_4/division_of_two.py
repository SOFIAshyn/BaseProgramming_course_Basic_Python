def division_of_two(number, divisor):
    '''(int, int) -> boolean
    Function check if (number > 0) % (2 <= divisor =< 9).
    >>> division_of_two(81, 9)
    True
    >>> division_of_two(81, 2)
    False
    >>> division_of_two(11, 6)
    False
    '''
    if (number > 0) and (divisor <= 9) and (divisor >= 2):
        if (number % divisor == 0):
            return True
        else:
            return False

print(division_of_two(-11, 6))
