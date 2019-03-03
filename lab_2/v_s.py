import math

r = eval(input())

v = 4/3 * math.pi * r ** 3
a = 4 * math.pi * r ** 2

print("V = ", round(v, 3) if v % 1 != 0 else int(round(v, 3)))

if round(a, 3)%1 == 0.0:
    print("A = %d" % round(a))
else:
    print("A = ", round(a, 3) if a % 1 != 0 else int(round(a, 3)))
