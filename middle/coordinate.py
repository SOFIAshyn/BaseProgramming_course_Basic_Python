def length(t):
    x1, y1 = t[0]
    x2, y2 = t[1]
    return ((x2**2 - x1**2) + (y2**2 - y1**2))**(1.0/2.0)

def find_ox(tup):
    x1, y1 = tup[0]
    x2, y2 = tup[1]
    len_ox = abs(x2 - x1)
    return len_ox

n = int(input("Enter n: "))
lst_coordinates = []
for i in range(n):
    x1 = int(input("X1 = "))
    y1 = int(input("Y1 = "))
    x2 = int(input("X2 = "))
    y2 = int(input("Y2 = "))
    lst_coordinates.append([(x1, y1), (x2, y2)])

for i, para in enumerate(lst_coordinates):
    lst_coordinates[i].append(find_ox(para))

all_lenght = []
for i, el in enumerate(lst_coordinates):
    all_lenght.append(el[-1])
    lst_coordinates[i] = tuple(el)

my_max = all_lenght[0]
i_max = 0
for i, el in enumerate(all_lenght):
    if my_max < el:
        my_max = el
        i_max = i

para = lst_coordinates[i_max][:2]
hipotenusa = lst_coordinates[i_max]
res = [para, my_max, length(hipotenusa)]
print("Coordinates = ", res[0], "\nlen on ox = ", res[1], "\nlen of section = %.4f" % res[2])


