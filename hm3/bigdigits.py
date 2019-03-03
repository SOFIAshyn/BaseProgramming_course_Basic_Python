import sys


def return_digits(number):
    """
    (str) -> str

    Return number in creative way.

    >>> print(return_digits("41072819"))
       4   1   000  77777 222  888  1  9999
      44  11  0   0     72   28   811 9   9
     4 4   1 0     0   7 2  2 8   8 1 9   9
    4  4   1 0     0  7    2   888  1  9999
    444444 1 0     0 7    2   8   8 1     9
       4   1  0   0 7    2    8   8 1     9
       4  111  000  7    22222 888 111    9
    """
    res = ""
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(number):
            symb = int(number[column])
            digit = Digits[symb]
            line += digit[row].replace("*", str(symb))
            column += 1
        row += 1
        if row != 7:
            res += line + "\n"
        else:
            res += line
    return res



Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    res = return_digits(digits)
    print(res)
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)


import doctest
doctest.testmod()
