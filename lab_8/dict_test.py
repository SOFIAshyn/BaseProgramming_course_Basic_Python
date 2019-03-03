lst = [1, 2, 3, 4, 5]
dct ={"ucu": 100, "apps": 200, "chototam": 300, 1: 3}

for i in dct.keys():
    print (i)
print(type(dct.keys()))

for i in dct.values():
    print (i)
print(type(dct.values()))

for key, value in dct.items():
    print(key, value)
print(type(dct.values()))
