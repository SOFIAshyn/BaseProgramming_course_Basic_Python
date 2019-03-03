def bool_mult(lst1, lst2):
    lst2_rev = []
    mult = []
    for i in range(len(lst2)):
        lst2_rev.append([])
        mult.append([])

    for i in range(len(lst2)):
        for k in range(len(lst2)):
            lst2_rev[i].append(lst2[k][i])
    print(lst1, lst2_rev)

    n = len(lst1)
    for i in range(n):
        for k in range(n):
            check = 0
            temp = 0
            for j in range(n):
                check_t = 0
                if lst1[i][j] == lst2_rev[k][j] and lst1[i][j] == 1:
                    check_t = 1
                temp += check_t
            if temp >= 1:
                check = 1
            mult[i].append(check)
    for i in mult:
        print(i)
    print(mult)




r = [[0, 0, 1], [1, 1, 0], [0, 1, 1]]
s = [[0, 0, 1], [1, 1, 0], [0, 1, 1]]
# for i in lst1
bool_mult(s, r)
