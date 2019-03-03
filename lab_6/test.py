# import os
#
# path = 'my_dir'
# date_from_name = {}
# for name in os.listdir(path):
#     fullname = os.path.join(path, name)
#     if os.path.isfile(fullname):
#         date_from_name[fullname] = os.path.getmtime(fullname)
#
# print(date_from_name)

def weekdayByNumber(number):
    """int -> str

    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]

    >>> weekdayByNumber(3)
    'thu'
    """
    week_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    res = week_days[number]
    return res
