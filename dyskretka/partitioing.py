n = int(input("Enter a number of elements: "))
lst = []
a = 45

letter = 97
for i in range(n):
    lst.append(chr(letter))
    letter += 1
import intertools
print(intertools.combinations(lst))

part = 1
partitioning = []










#
# while n != 0:
#     for i in range(n):
#         partitioning.append(lst[i] + [lst[i + k] for k in range(part)])
#     n -= 1
#     part += 1
# print(partitioning)
