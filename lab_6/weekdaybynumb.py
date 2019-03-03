def weekdayByNumber(number):
    """int -> str

    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]

    >>> weekdayByNumber(3)
    'thu'
    """
    week_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    res = number

    return week_days[res]

print(weekdayByNumber(3))
