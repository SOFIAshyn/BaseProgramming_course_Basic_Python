def weekdayByNumber(number):
    """int -> str

    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]

    >>> weekdayByNumber(3)
    'thu'
    """
    assert(0 <= number <= 6), "You should change format of input, \
    you have an error AssertionError"
    week_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    res = number

    return week_days[res]


def getWeekday(date):
    """str -> int

    Return an integer representing a weekday(0 represents monday and so on)
    read about algorithm at
    http://vidpo.net/de-znajti-metod-algoritm-viznachennja-dnja-tizhnja.html
    date : a string of form "day.month.year"
    if the date is invalid raises AssertionError with corresponding message

    >>> getWeekday("12.08.2015")
    2
    >>> getWeekday("28.02.2016")
    6
    """
    assert(date[2], date[6] == "."), "You should change format of input, \
    you have an error AssertionError"
    day, month, year = map(int, date.split("."))
    m_op = (14 - month) // 12
    y_op = year - m_op
    m_y_op = month + 12 * m_op - 2
    day_numb = (day + y_op + y_op // 4 - y_op // 100 + y_op // 400 +
    (31 * m_y_op) // 12) % 7
    day_numb -= 1
    if day_numb == -1:
        day_numb = 6

    return day_numb


def monthrangeForCalendar(month, year):
    """(int, int) -> int

    Return the number of days in the month

    >>> monthrangeForCalendar(2, 2016)
    29
    >>> monthrangeForCalendar(8, 1999)
    31
    """
    if month == 2:
        if (year - 1584) % 4 == 0:
            leap_year = True
        if leap_year:
            return 29
        else:
            return 28
    if month <= 7 and month % 2 != 0 or month > 7 and month % 2 == 0:
        return 31
    if month < 7 and month % 2 == 0 or month > 7 and month % 2 != 0:
        return 30


def transform_calendar(month, year):
    """(int, int) -> str

    Return a string representing a calendar for given month and year
    (horisontal)

    month : an integer in range[1 , 12]
    year : an integer (strictly speaking the algorithm in getWeekday works
           correctly only for Gregorian calendar, so year must be greater
           than 1583)
    when arguments are invalid raises AssertionError with corresponding message

    >>> print(transform_calendar(3 , 2016))
    mon tue wed thu fri sat sun
         1   2   3   4   5   6
     7   8   9   10  11  12  13
     14  15  16  17  18  19  20
     21  22  23  24  25  26  27
     28  29  30  31
    """
    assert(0 <= month <= 12, year >= 1583), "You should write numbers, \
    you have AssertionError"
    line_cal = ""
    all_cal = ""
    each_week = {}
    first_one = True
    for name_day in range(7):
        line_cal += weekdayByNumber(name_day)
        if name_day != "sun":
            line_cal += " "
    line_cal += "\n"
    first_pos = getWeekday("01.%.2d.%d" % (month, year))
    line_cal += "    " * first_pos + " "
    pos = first_pos
    for day in range(1, monthrangeForCalendar(month, year) + 1):
        if len(str(day)) == 1:
            two_or_one_symb = " " * 3
        else:
            two_or_one_symb = " " * 2
        line_cal += str(day) + two_or_one_symb
        if pos == 6:
            pos = 0
            line_cal += "\n" + " "
        else:
            pos += 1
    all_cal += line_cal
    return str(all_cal)


def getCalendar(month, year):
    """(int, int) -> str

    Return a string representing a calendar for given month and year
    (vertical)

    month : an integer in range[1 , 12]
    year : an integer (strictly speaking the algorithm in getWeekday works
           correctly only for Gregorian calendar, so year must be greater
           than 1583)
    when arguments are invalid raises AssertionError with corresponding message

    >>> print(getCalendar(8 , 2015))
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30
    """
    assert(1 <= month <= 12 or year >= 1583), "You should write numbers, \
    you have an AssertionError"
    each_week = {}
    all_cal = ""
    first_day = False
    for week in range(7):
        each_week[weekdayByNumber(week)] = []
        for day in range(1, monthrangeForCalendar(month, year) + 1):
            data_input = str("%.2d.%.2d.%d" % (day, month, year))
            if week == getWeekday(data_input):
                each_week[weekdayByNumber(week)].append(str(day))
        for week_key in each_week.keys():
            str_cal = week_key
            if first_day is False:
                if each_week[week_key][0] != "1":
                    str_cal += " " * 2
                if each_week[week_key][0] == "1":
                    first_day = True
            for i in each_week[week_key]:
                len_two_or_one = 1
                if int(each_week["mon"][0]) >= 4 and len(i) == 1:
                    if int(i) >= int(each_week["mon"][0]):
                        len_two_or_one = 2
                str_cal += " " * len_two_or_one + i
            if week_key != "sun":
                str_cal += "\n"
        all_cal += str_cal
    return str(all_cal)


if __name__ == '__main__':
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print (getCalendar(month, year))
        print (transform_calendar(month, year))
    except ValueError as err:
        print(err)

    import doctest
    print(doctest.testmod())
