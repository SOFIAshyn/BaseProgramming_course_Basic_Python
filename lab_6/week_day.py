def weekdayByNumber(number):
    """
    number : an integer in range [0, 6]
    return : a string representing a weekday
             (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    
    >>> weekdayByNumber(3)
    "thu"
    """
    assert ((number >= 0) and (number <= 6)),\
            "Invalid argument: number out of range"
    
    if number == 0: return "mon"
    if number == 1: return "tue"
    if number == 2: return "wed"
    if number == 3: return "thu"
    if number == 4: return "fri"
    if number == 5: return "sat"
    if number == 6: return "sun"
	
def getWeekday(date):
    """
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError with corresponding message
    return : an integer representing a weekday(0 represents monday and so on)
    read about algorithm at
    http://vidpo.net/de-znajti-metod-algoritm-viznachennja-dnja-tizhnja.html
                                            
    >>> getWeekday("12.08.2015")
    2
    >>> getWeekday("28.02.2016")
    6                                      
    """
    day = int(date.split(".")[0])
    month = int(date.split(".")[1])
    year = int(date.split(".")[2])

    assert(day > 0), "Invalid date: day <= 0"
    assert(month > 0), "Invalid date: month <= 0"
    assert(month <= 12), "Invalid date: month > 12"
    assert(year > 1583), "Invalid date: year <= 1583"

    if (month == 1) or (month == 3) or (month == 5) or (month == 7)\
                    or (month == 8) or(month == 10) or (month == 12):
        assert (day <= 31), "Invalid date: day > 31"
    elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
        assert (day <= 30), "Invalid date: day > 30"
    elif ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 ==0):
        assert (day <= 29), "Invalid date: day > 29"
    else:
        assert (day <= 28), "Invalid date: day > 28"
    
    if month <= 2:
        day += 3
        year -= 1
        
    weekdayNumber = (day + year + (year // 4) - (year // 100)
                     + (year // 400) + (31 * month + 10) // 12) % 7
    return weekdayNumber

print("I don't know what is wrong!")

