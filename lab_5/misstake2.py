def repeated_digits(n):
    """
    int -> bool

    Return return True if the number n has at least one pair of sequentially
    repeating digits and False otherwise

    >>> 77
    True

    >>> 123
    False

    >>> -123
    False

    """
    n = int(n)
    if n < 0:
        n *= (-1)
    remaining_digits = n
    while remaining_digits // 10 > 0:
        first_digit = remaining_digits % 10
        tens_digit = (remaining_digits // 10) % 10
        if first_digit == tens_digit:
            print(n,"has repeated digits!")
            return True
        remaining_digits = remaining_digits//10
    print(n,"has no repeated digits...")
    return False

print(repeated_digits(-123))
