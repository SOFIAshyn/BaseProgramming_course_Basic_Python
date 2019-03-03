import calendar
import datetime

each_week = {
'mon': ['5', '12', '19', '26'],
'tue': ['6', '13', '20', '27'],
'wed': ['7', '14', '21', '28'],
'thu': ['1', '8', '15', '22', '29'],
'fri': ['2', '9', '16', '23', '30'],
'sat': ['3', '10', '17', '24', '31'],
'sun': ['4', '11', '18', '25']}

for each in each_week.keys():
    str_cal = each
    if (each_week["sun"][0] < each_week[each][0]):
        str_cal += "  "
    for i in each_week[each]:
        str_cal += " " + i
    str_cal += "\n"
    #print(each, a[each])
    print (str_cal, end ="")

# print(calendar.monthcalendar(2016, 10))
#
# cal = calendar.TextCalendar(calendar.TUESDAY)
# cal_format = cal.formatmonth(2016, 10, 0, 0)
#
# print(cal_format)
#
# print(calendar.monthrange(2016, 5)[1])

# for day in range(1, calendar.monthrange(2017, 1)[1] + 1):
#     year, month, day = str(datetime.date(2017, 1, day)).split("-")
#     data_input = day + "." + month + "." + year
#     print(type(data_input))

# week_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
# print week_days.index("mon")

#
# data_input = str(datetime.date(2017, 8, 2)).replace("-", ".")
# print(data_input)
#
# date = "28.09.2018"
#
# day, month, year = map(int, date.split("."))
# print(day)
# print(month)
# print(year)
# print(calendar.weekday(year, month, day))

# for month in range(1, 13):
#     cal = calendar.monthcalendar(2016, month)
#     for i in cal:
#         if i[calendar.TUESDAY]:
#             print(i[calendar.TUESDAY], end = " ")
#     print('\n')

# def labor_days(year, month):
#     cal = calendar.Calendar()
#     cal = cal.monthdatescalendar(year, month)
#     for week in cal:
#         if week[1].month == month:
#             print(week[1])
#
# print(labor_days(2016, 10))
# number = 0
# week_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
# res = number - 1
# if res == -1:
#     res = 6
# print(week_days[res])
#
# if week == getWeekday(data_input):
#     each_week[weekdayByNumber(week)].append(str(day))
#
# calendar_string = ""
# for i in range(1, 8):
# for element in each_week:
# print(element)
# return(a)
# print(res = 7 if res == -1, res = number-1)
