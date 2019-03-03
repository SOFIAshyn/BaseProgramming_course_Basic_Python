def find_max_area(s):
    my_max = 0
    for a in range(1, s):
        for b in range(1, s):
            if a + b == s:
                if a * b > my_max:
                    my_max = a * b
                    my_max_tup = tuple([a, b])
    return s, my_max_tup


def to_file(res):
    file = open("sq_rectangle.txt", "w+")
    for i in res:
        file.write(str(i[0]) + '\t' + str(i[1][0]) + ' ' + str(i[1][1]) + '\n')
    file.close()


def main():
    n = input("Enter n: ")
    try:
        int(n)
    except ValueError as err:
        print("Print integer", err)
    lst_s = []
    for i in range(int(n)):
        s = int(input("Write area: "))
        lst_s.append(s)

    res = []
    for s in lst_s:
        res.append(find_max_area(s))
    to_file(res)


if __name__ == "__main__":
    main()
