def read_crossword(path):
    d = {}
    lst_val = []
    lst_keys = []
    f =  open(path, "r")
    for line in f.readlines():
        line = line.replace("\n", "")
        if line.startswith("("):
            line = list((line.replace(")", "").replace("(", "")).split())
            lst_val.append(line)
        else:
            lst_keys.append(line)
    for el in range(len(lst_keys)):
        d[lst_keys[el]] = lst_val[el]
    return(d)
#print(read_crossword("crossword_3.txt"))

def print_crossword(crossword):
    lst_v = []
    lst_k = []
    for key in crossword.keys():
        for i in range(len(key)):
            lst_k.append(key[i])
    print(lst_k)
    for val in crossword.values():
        for i in val:
            i = list(i.replace(",", ""))
            lst_v.append(i)
    print(lst_v)

    prob = []
    for i in range(0, 8):
        prob.append(list())

    for j in range(0, 8):
        for i in range(0, 8):
            prob[j].append(" ")

    for el in range(len(lst_v)):
        for i in range(0, 8):
            for j in range(0, 8):
                if i == int(lst_v[el][0]) and j == int(lst_v[el][1]):
                    prob[i][j] = lst_k[el]

    for lst in prob:
        for el in lst:
            print(el, end = " ")
        print()


print_crossword(read_crossword("crossword_3.txt"))
