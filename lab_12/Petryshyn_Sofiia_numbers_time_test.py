import timeit


# from functools import lru_cache

# @lru_cache(maxsize=1000)

# FIBONACHI FUNCTIONS
def fib_rec(n, depth=0, verbose=False):
    """
    (int, int, bool) -> int

    Return fibonachi number

    >>> fib_rec(5, depth=0, verbose=False)
    5
    """
    if verbose:
        print(" " * depth, "fib_rec_true(", n, " )")
    if (n <= 2):
        result = 1
    else:
        result = fib_rec(n - 1, depth + 1, verbose) + \
                 fib_rec(n - 2, depth + 1, verbose)
    if verbose:
        print(" " * depth, " --> ", result)
    return result


def fib_iter(n, verbose=False):
    """
    (int, bool) -> int

    Return fibonachi number

    >>> fib_iter(5, verbose=False)
    5
    """
    if verbose == False:
        fib1 = 1
        fib2 = 1
        for i in range(n - 2):
            fib1, fib2 = fib2 + fib1, fib1
        return fib1
    else:
        fib1 = 1
        fib2 = 1
        print(1, " --> ", fib1)
        print(2, " --> ", fib2)
        for i in range(n - 2):
            fib1, fib2 = fib2 + fib1, fib1
            print(i + 3, " --> ", fib1)
        return fib1


# FACTORIAL FUNCTIONS

def fact_rec(n, depth=0, verbose=False):
    """
    (int, int, bool) -> int

    Return factorial number

    >>> fact_rec(5, depth=0, verbose=False)
    120
    """
    # if verbose == False:
    #     if n == 0:
    #         return 1
    #     return n * fact_rec(n - 1)
    # else:
    if verbose is True:
        print("  " * depth, "factorial(", n, ")")
    if n < 2:
        result = 1
    else:
        result = n * fact_rec(n - 1, depth + 1, verbose)
    if verbose is True:
        print("  " * depth, "-->", result)
    return result


def fact_iter(n, verbose=False):
    """
    (int, bool) -> int

    Return factorial number

    >>> fact_iter(5, verbose=False)
    120
    """
    if verbose == False:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i
            print("factorial(", i, ") --> ", res)
        return res


def numbers_time_test(n, func_numb, rec_or_iter, verbose):
    """
    (str, str, str, str) -> None

    Call function that chose user

    >>> print(numbers_time_test("5", "nothing", "iteration", "True"))
    None
    """
    # FACTORIAL
    if func_numb == "factorial":
        if rec_or_iter == "recursion":
            if verbose == "True":
                time1 = timeit.default_timer()
                print(fact_rec(int(n), verbose=True))
                duree = timeit.default_timer() - time1
                print("Time of recursion factorial: ", duree)
            else:
                time1 = timeit.default_timer()
                fact_rec(int(n), verbose=False)
                duree = timeit.default_timer() - time1
                print("Time of recursion factorial: ", duree)
        elif rec_or_iter == "iteration":
            if verbose == "True":
                time1 = timeit.default_timer()
                print(fact_iter(int(n), verbose=True))
                duree = timeit.default_timer() - time1
                print("Time of iteration factorial: ", duree)
            else:
                time1 = timeit.default_timer()
                fact_iter(int(n), verbose=False)
                duree = timeit.default_timer() - time1
                print("Time of iteration factorial: ", duree)

    # FIBONACHI
    elif func_numb == "fibonachi":
        if rec_or_iter == "recursion":
            if verbose == "True":
                time1 = timeit.default_timer()
                print(fib_rec(int(n), verbose=True))
                duree = timeit.default_timer() - time1
                print("Time of recursion fibonaci: ", duree)
            elif verbose == "False":
                time1 = timeit.default_timer()
                fib_rec(int(n), verbose=False)
                duree = timeit.default_timer() - time1
                print("Time of recursion fibonaci: ", duree)
        elif rec_or_iter == "iteration":
            if verbose == "True":
                time1 = timeit.default_timer()
                print(fib_iter(int(n), verbose=True))
                duree = timeit.default_timer() - time1
                print("Time of iteration fibonaci: ", duree)
            elif verbose == "False":
                time1 = timeit.default_timer()
                fib_iter(int(n), verbose=False)
                duree = timeit.default_timer() - time1
                print("Time of iteration fibonaci: ", duree)
        else:
            return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    func_numb = input("Write 'factorial' or 'fibonachi': ")
    rec_or_iter = input("Write 'recursion' or 'iteration': ")
    verbose = input("Write 'True' or 'False': ")
    n = input("Write number you want to calculate: ")
    time1 = timeit.default_timer()
    numbers_time_test(n, func_numb, rec_or_iter, verbose)
    duree = time1 - timeit.default_timer()
