def code_gray():
    dn = 2
    b = []
    for day in range(dn, dn + 11):
        #encode
        g = bin(day ^ (day >> 1))[2:]
        print("Gray code for ", day, " is ", g)
        #decode_gray
        b.insert(0, g[0])
        for i in range(1, len(g)):
            b.insert(i, str(int(g[i]) ^ int(b[i - 1])))
        print("Decoded :", int("".join(b), 2))

code_gray()
