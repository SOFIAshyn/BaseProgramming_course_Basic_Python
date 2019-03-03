def factorial(n):
    """ int -> int
    Return factorial of n

    #TODO
    >>> factorial(5)
    120

    >>> factorial(0)
    1
    """
    n = int(n)
    if n == 0:
        return 1
    else:
        result = n
        for smaller_integer in range(1, n):
            result *= smaller_integer
        return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(factorial(5))
