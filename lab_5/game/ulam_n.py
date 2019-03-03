def ulam_n(num):
    ''' (int) -> bool

    Return if the number is Ulan number

    #TODO:
        >>> ulam_n(18)
        >>> True
        >>> ulan_n(131)
        >>> True
        >>> ulan_n(5)
        >>> False
    '''
    ulam_num = [1, 2, 3]

    for i in range(4, num + 1):
        count = 0
        for j in range(1, (i//2) + 1):
            if j in ulam_num and i-j in ulam_num:
                if j != i - j:
                    if count != 1:
                        ulam_num.append(i)
                    count += 1
                if count > 1:
                    ulam_num.pop()
                    break

    if ulam_num[-1] == num:
        return True
    else:
        return False

#print(ulam_n(18))