try:
    n = int(input())
except ValueError as err:
    print("Error ", err)

import string

s = set(map(int, list(filter(lambda el: el.isdigit(), input().split()))))
com = 0
try:
    com = int(input())
except ValueError as arr:
    print(arr)

lst = set()
for i in range(com):
    lst.add(tuple(x for x in input().split()))
for el in lst:
    try:
        if el[0] == "remove":
            s.remove(int(el[1]))
        elif el[0] == "pop":
            s.pop()
        elif el[0] == "discard":
            s.discard(int(el[1]))
    except ValueError as err:
        print("Error ", err)
    except IndexError as arr1:
        print("err ", err)
print(s)
