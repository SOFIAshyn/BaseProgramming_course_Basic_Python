def read_crossword(path):
    lst_keys = []
    lst_val = []
    dic = {}
    file = open(path, "r")
    for line in file:
        if line.startswith("("):
            lst_val.append(line.replace("(", "").replace(")", "").split())
        else:
            lst_keys.append(line[:-1])
    for i in range(len(lst_val)):
        dic[lst_keys[i]] = lst_val[i]
    for item in dic.values():
        for i in range(len(item)):
            item[i] = (int(item[i][0]), int(item[i][-1]))
    file.close()
    return dic

def print_crossword(crossword):
    lst_k = []
    lst_v = []
    for key in crossword.keys():
        lst_k.append(key)
    for val in crossword.values():
        lst_v.append(val)

    cros_prob = []
    for el in range(8):
        cros_prob.append([])
    for item in cros_prob:
        for i in range(8):
            item.append(" ")

    for el in range(len(lst_v)):
        for tup in range(len(lst_v[el])):
            for i in range(8):
                for j in range(8):
                    if lst_v[el][tup][0] == i and lst_v[el][tup][1] == j:
                        cros_prob[i][j] = lst_k[el][tup]
    for lst in cros_prob:
        for el in lst:
            print(el, end=" ")
        print()


def main():
    cros = read_crossword("crossword_1.txt")
    print_crossword(cros)

main()