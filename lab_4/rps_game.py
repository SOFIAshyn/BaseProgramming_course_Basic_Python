def rps_game(lst):
    '''(list) -> boolean
    Function to find a winner for game "Rock, Scissors, Paper"

    >>> rps_game(['SS', 'RS', 'PS'])
    [(False, False), (True, False), (False, True)]

    >>> rps_game(['PR'])
    [(True, False)]
    '''

    result_lst = []
    match_partFT = (False, True)
    match_partTF = (True, False)
    for match in lst:
        match = match.lower()
        if match[0] == match[1]:
            match_part = (False, False)
            result_lst.append(match_part)
        elif match == "sp" or match == "ps":
            if match[0] == "s":
                result_lst.append(match_partTF)
            else:
                result_lst.append(match_partFT)
        elif match == "rp" or match == "pr":
            if match[0] == "p":
                result_lst.append(match_partTF)
            else:
                result_lst.append(match_partFT)
        elif match == "sr" or match == "rs":
            if match[0] == "r":
                result_lst.append(match_partTF)
            else:
                result_lst.append(match_partFT)
    return result_lst

rps_game(['RS', 'pp'])
