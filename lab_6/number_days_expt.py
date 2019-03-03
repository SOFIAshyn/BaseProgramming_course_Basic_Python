def number_days(month, year):
    '''
    (int, int) -> (int)

    Return number of days in the month of the year.
    Preconditions: year > 1583
    
    >>> number_days(2, 2016)
    29

    >>> number_days(2, 1900) 
    28

    >>> number_days(5, 2000) 
    31

    >>> number_days(11, 1968) 
    30
    '''
    try:
        
        month, year = int(month), int(year)
        assert ( 1<= month <= 12)

        if (month == 1) or (month == 3)\
                    or (month == 5)\
                    or (month == 7)\
                    or (month == 8)\
                    or (month == 10)\
                    or (month == 12):
            return(31)

        elif (month == 4) or (month == 6)\
                      or (month == 9)\
                      or (month == 11):
            return(30)

        elif ((year % 4 == 0) and (year % 100 != 0))\
                             or (year % 400 ==0):

            return(29)
        else:
            return(28)
        
    except ValueError:
        print("Please, type integers")
    except AssertionError:
        print("Please, type correct month number (from 1 to 12)")
        
print(__name__)
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
