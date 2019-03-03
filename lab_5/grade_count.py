def  grade_count(grades):
    ''' list[int, int, int, int, int] -> tuple (float, string)
    Return cortege of avarage grade and ECTS mark

    >>> grade_count([85, 90, 67, 70, 87])
    (79.8, 'C')

    >>> grade_count([97, 93, 84, 78, 80])
    (86.4, 'B')
    '''

    sum = 0
    for i in grades:
        if 0 <= i <= 100:
            sum += i
        else:
            return (None, None)
    letter_grade = 0
    percent_grade = round(sum / 5, 2)
    if 90 <= percent_grade <= 100:
        letter_grade = "A"
    elif 82 <= percent_grade <= 89:
        letter_grade = "B"
    elif 75 <= percent_grade < 82:
        letter_grade = "C"
    elif 67 <= percent_grade < 75:
        letter_grade = "D"
    elif 60 <= percent_grade < 67:
        letter_grade = "E"
    elif 0 <= percent_grade < 60:
        letter_grade = "F"
    return (percent_grade, letter_grade)


print(grade_count([97, 93, 84, 78, 80]))
print(grade_count([90, 87, 93, 68, 71]))
print(grade_count([101, 47, 60, 68, 71])) #
print(grade_count([-90, 87, 90, 98, 91])) #
