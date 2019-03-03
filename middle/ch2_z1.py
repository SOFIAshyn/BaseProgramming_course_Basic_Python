from math import pi


def filter_sq(lst):
    if lst[1] >= lst[2]:
        sq = lst[1]
    else:
        sq = lst[2]
    return sq


def check_l_aq(R, sq):
    if pi * R ** 2 <= sq:
        return 1
    return 0


def main():
    n = int(input("Write n: "))
    assert n > 0, "Write n > 0"
    R = int(input("Write radius: "))
    assert R > 0, "Write R > 0"

    lst_three = []
    for i in range(n):
        l = (input("Print 1 numbers: "))
        s1 = (input("Print 2 numbers: "))
        s2 = (input("Print 3 numbers: "))
        try:
            l = int(l)
            s1 = int(s1)
            s2 =int(s2)
        except ValueError:
            print("Write only int! ")

        if l > R + 17 * R / 100:
            lst_three.append((l, s1, s2))
    filtered_lst = []
    for three in lst_three:
        max_s = filter_sq(three)
        if check_l_aq(R, max_s):
            filtered_lst.append(three)
    print(lst_three)

main()
