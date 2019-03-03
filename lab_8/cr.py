def read_crossword(path):
    """
    (str) -> list

    Return dictionary key = word and coordinates


    """
    d = {}
    lst_val = []
    lst_keys = []
    f = open(path, "r")
    for line in f.readlines():
        line = line.replace("\n", "")
        if line.startswith("(") is not True:
            lst_keys.append(line)
    for i in lst_keys:
        for line in f.readlines():
            line = line.replace("\n", "")
            if line.startswith("("):
                line = line.replace("(", "").replace(")", "").split(",")
                d[i] = line
    f.close()
    # for i in lst_keys:
    #     for j in lst_val:
    #         d[i] = j
    return(d)

a = read_crossword("crossword_3.txt")
print(a)
def print_crossword(crossword):
    """
    (dict) -> None

    Print calendar
    """
    lst_one_val = []
    for val in crossword.values():
        val = val.replace("(", "").replace(")", "").split()
        for el in range(len(val)):
            val[el] = val[el].split(',')
    # for key in crossword.keys():
    #     for letter in key:
    #         for value in crossword.values():
    #             pass
    print(crossword)



print_crossword(a)
