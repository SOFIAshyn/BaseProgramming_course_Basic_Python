# def getWeekday(date):
#     """str -> int
#
#     Return an integer representing a weekday(0 represents monday and so on)
#     read about algorithm at
#     http://vidpo.net/de-znajti-metod-algoritm-viznachennja-dnja-tizhnja.html
#     date : a string of form "day.month.year"
#     if the date is invalid raises AssertionError with corresponding message
#
#     >>> getWeekday("12.08.2015")
#     2
#     >>> getWeekday("28.02.2016")
#     6
#     """
#     day, month, year = map(int, date.split("."))
#     m_op = (14 - month) // 12
#     y_op = year - m_op
#     m_y_op = month + 12 * m_op - 2
#     day_numb = (day + y_op + y_op // 4 - y_op // 100 + y_op // 400 + (31 * m_y_op) // 12) % 7
#     day_numb -= 1
#     if day_numb == -1:
#         day_numb = 6
#     return day_numb
#
# print(getWeekday("25.10.2018"))

def monthrangeForCalendar(month, year):
    if month == 2:
        if (year - 1584) % 4 == 0:
            leap_year = True
        if leap_year:
            return 29
        else:
            return 28
    if month <= 7 and month % 2 != 0 or month > 7 and month % 2 ==0:
    # in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month < 7 and month % 2 == 0 or month > 7 and month % 2 != 0:
    # in [4, 6, 9, 11]:
        return 30


print(monthrangeForCalendar(7, 2016))
