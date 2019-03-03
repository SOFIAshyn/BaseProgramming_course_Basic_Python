lst = []
a = ''
while a != set():
    a = set(map(int, input("write: ").split()))
    if a != set():
        lst.append(a)

for i in range(len(lst)):
    if lst[i] == lst[-1]:
        t = lst[i].difference(lst[0])
    else:
        t = lst[i].difference(lst[i + 1])
    print("difference: ", t)

print(lst)
