# def prime_number_faster(num):
#     if (num < 2):
#         return False
#     if (num == 2):
#         return True
#     if (num % 2 == 0):
#         return False
#     max_factor = round(num ** 0.5)
#     print(num, "max = ", max_factor)
#     for factor in range(3, max_factor + 1, 2):
#         print("factor = ", factor)
#         if (num % factor == 0):
#             return False
# return True
#
# def nth_prime(n):
#     found = 0
#     guess = 0
#     while (found <= n):
#         guess += 1
#     if (prime_number_faster(guess)):
#         found += 1
#     return guess
#
# # list of the primes
# for num in range(10):
#     print(num, nth_prime(num))

# text = """
# tt0000001	short	Carmencita	Carmencita	0	1894 \N	1	Documentary,Short tt0000002	short	Le clown et ses chiens	Le clown et ses chiens	0	1892	\N	5	Animation,Short
# tt0000003	short	Pauvre Pierrot	Pauvre Pierrot	0	1892	\N	4	Animation,Comedy,Romance
# tt0000004	short	Un bon bock	Un bon bock	0	1892	\N	\N	Animation,Short
# tt0000005	short	Blacksmith Scene	Blacksmith Scene	0	1893	\N	1	Comedy,Short
# tt0000006	short	Chinese Opium Den	Chinese Opium Den	0	1894	\N	1	Short
# tt0000007	short	Corbett and Courtney Before the Kinetograph	Corbett and Courtney Before the Kinetograph	0	1894	\N	1	Short,Sport
# tt0000008	short	Edison Kinetoscopic Record of a Sneeze	Edison Kinetoscopic Record of a Sneeze	0	1894	\N	1	Documentary,Short
# tt0000009	movie	Miss Jerry	Miss Jerry	0	1894	\N	45	Romance
# tt0000010	short	Exiting the Factory	La sortie de l'usine Lumière à Lyon	0	1895	\N	1	Documentary,Short
# tt0000011	short	Akrobatisches Potpourri	Akrobatisches Potpourri	0	1895	\N	1	Documentary,Short
# tt0000012	short	The Arrival of a Train	L'arrivée d'un train à La Ciotat	0	1896	\N	1	Documentary,Short
# tt0000013	short	The Photographical Congress Arrives in Lyon	Neuville-sur-Saône: Débarquement du congrès des photographes à Lyon	0	1895	\N	1	Documentary,Short
# tt0000014	short	The Sprinkler Sprinkled	L'arroseur arrosé	0	1895	\N	1	Comedy,Short
# tt0000015	short	Autour d'une cabine	Autour d'une cabine	0"""
#
# import collections
# a = collections.Counter(text.strip().split('\t')).most_common(3)

# def trace(L):
#     for i in range(len(L)):
#         L[i] = str(L[i]) * L[i]
#     return sum([int(val) for val in L])
# print(trace(list(range(1, 3))))


# READ FROM FILE
# file = open("text.txt", 'r+')
# print(file.readline(), '\n')
# print(file.read())
# print(file.readline(), '\n')
# print(file.readlines(), '\n')
# print("where is we?")
# print(file.read(), '\n')
# print(list(x for x in file.read()), '\n')
# file.write(r"\n{i'm here}----")

# ???????????????????????? LISTS
# a = [2, 2, 2]
# print("a = ", a)
# b = a
# print("a = b = ", b)
# a = [3, 3, 3]
# print("a = ", a)
# print("a = [3] * 3 -> b = ", b)
#
# import copy
# c = copy.copy(a)
# print("\na = ", a)
# print("c = copy(a)", c)
# a = [4, 4,4]
# print("a = ", a)
# print("c = copy(a)", c)


# def trace(L):
#     for i in range(len(L)):
#         L[i] = [L[i]] * L[i]
#     return sum([sum(val) for val in L])
# print(trace(list(range(3))))


# import collections
#
# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
#
# text_lst = text.split()
#
#
#
# dict = {}
#
# for el in collections.Counter(text_lst).most_common(10):
#     dict[el[0]] = el[1]
# print(dict)
#
# # s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# #
# # d = defaultdict(list)
# #
# # for key, val in s:
# #     d[k].append(val)
# # print(d)
# # print(d.items())