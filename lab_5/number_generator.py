def number_generator(number, digit, position):
    ''' (number, number, number) -> number
    Returns a number with replaced digit of the number

    >>> number_generator(-3746, 7, 5)
    -703746

    >>> number_generator (3746, 5, 7)
    50003746
    '''
    if 0 <= digit <= 9 and position >= 0:
        res = ""
        k = 0
        if number < 0:
            number *= (-1)
            k = 1
        num_str = str(number)
        if position >= len(num_str):
            res = int(str(digit) + "0" * (position - len(num_str)) + num_str)
            if k == 1:
                res *= (-1)
            return(res)
        else:
            num_lst = []
            for i in num_str:
                if num_str.index(i) == (len(num_str) - position - 1):
                    if digit > int(i):
                        i = digit
                num_lst.append(i)
            for each in num_lst:
                res += str(each)
            res = int(res)
            if k == 1:
                res *= (-1)
            return res

print(number_generator(-3746, 7, 5))
print(number_generator(297, 2, 1))
