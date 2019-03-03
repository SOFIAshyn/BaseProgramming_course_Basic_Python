# max = int(input())
# i = 0
#
# while i < max:
#     i += 1
# print (i)

# num = int(input())
# root = 0
# pwr = 0
#
# for i in range(1, num):
#     for j in range(1, 6):
#         if i** j == num:
#             root = i
#             pwr = j
#             break
# if root == 0:
#     print("Error")
# print(root, ", ", pwr)

# x= 4
# for i in range(x):
#     print (i)
#     x = 5

# x = 4
# for i in range(x):
#     for j in range(x):
#         print (j)
#         x = 2

# total = 0
# for c in '123':
#     total += int(c)
# print(total)

s = input()
my_list = []
sum = 0
my_list.append(s.split('.'))
for i in range(3):
    int(my_list[i])
    sum += my_list[i]
print(sum)
