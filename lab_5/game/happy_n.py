def is_happy(num):
    ''' (int) -> bool

    Return if the number is happy number

    #TODO:
        >>> is_happy(13)
        >>> True
        >>> is_happy(167)
        >>> True
        >>> ulan_n(89)
        >>> False
    '''
    list_of_digit = []
    count = 1

    while (len(list_of_digit) >= 1) or (list_of_digit == []):
        list_of_digit = []
        sum = 0

        for each_digit in range(len(str(num))):
            list_of_digit.append(num % 10)
            num //= 10

        for each in list_of_digit:
            sum += each**2
        num = sum
        if num == 1:
            return True

        count +=1
        if count > 100:
            return False

    return False


#print(is_happy(2080))