def sq(n):
    print("squerance({})".format(n))
    if n == 1:
        s =  1
    else:
        s =  sq(n - 1) + 2 * (n - 1) + 1
    print(" ---> ", s)
    return s


import sys

sys.setrecursionlimit(100000)


def line(n, m):
    print("line({}, {})".format(n, m))
    if n == 1:
        res = 1
    else:
        res = n**m + line(n - 1, m)
    print(" --> ", res)
    return res

def rec3(n, m):
    if n > m:
        res = rec3(n-m, m)
    elif n < m:
        res = rec3(n, m-n)
    elif (n == m):
        res = n
    return res

# n = 0
# m = 0
# def rec4(my_str):
#     if len(my_lst) == 1:
#         if ()
#         return list(0, 0)
#     my_lst = list(filter(lambda i: i.isalpha(), list(x for x in my_str)))
#     del my_lst[len(my_lst) - 1]
#     return rec4("".join(my_lst))

    # if my_lst[len(my_lst) - 1].isupper():
    #     del my_lst[len(my_lst) - 1]
    #     rec4("".join(my_lst))
    #     return list(n + 1, m)
    # else:
    #     del my_lst[len(my_lst) - 1]
    #     rec4("".join(my_lst))
    #     return list(m, n + 1)

    #     rec4(my_str)
    #return lst[n-1]


    # if 65 <= ord(rec4(lst[n-1])) <= 91:
    #     return list(n + 1, m)
    # if 98 <= ord(rec4(lst[n-1])) <= 124:
    #     return list(n, m + 1)
    # else:
    #     return list(n, m)
    # return list([n + 1, m] if 65 <= odr(rec4(lst[n-1])) <= 91 elif 98 <= odr(rec4(lst[n-1])) <= 124 list([n, m  + 1])
import random

lst = []
for i in range(10):
    lst.append(random.randrange(0, 10))
print(lst)
random.shuffle(lst)
print(lst)

#
# print(sq(5))
# print(line(6, 3))
# print(rec3(2, 3))
# print(rec4("wAt’rh7rJjoa"))


