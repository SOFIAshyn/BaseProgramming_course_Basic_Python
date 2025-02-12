# def dict_reader_tuple(file_dict):
#     """
#     (str) -> set
#
#     Return set of lines from inputed file (name, number of pronunsiation,
#     sounds)
#     output: [('A', 1, ['AH0']), ('A.', 1, ['EY1']), ('A', 2, ['EY1']),
#     ('A42128', 1, ['EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T',
#     'UW1', 'EY1', 'T']), ('AAA', 1, ['T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1']),
#     ('AABERG', 1, ['AA1', 'B', 'ER0', 'G'])]
#
#     >>> print("Done")
#     Done
#     """
#     all = list()
#     with open(file_dict, "r") as file:
#         for line in file.readlines():
#             line = line.replace("\n", "")
#             temp = line.split()
#             sounds = list(i for i in temp[2:])
#             line = (temp[0], int(temp[1]), sounds)
#             all.append(line)
#     return all
#
#
# def dict_reader_dict(file_dict):
#     """
#     (set) -> dict
#
#     Return dictionary with name key, where items is sounds of the word.
#
#     output: {'A.': {('EY1',)}, 'A': {('AH0', 'F', 'AO1', 'R', 'T'),
#           ('EY1', 'F', 'AO1', 'R', 'T'), ('EY1', 'G', 'AO1', 'R', 'T')}}
#
#     >>> print("Done")
#     Done
#     """
#     all = set()
#     dict_keyname = {}
#     with open(file_dict, "r") as file:
#         for line in file.readlines():
#             line = line.replace("\n", "")
#             temp = line.split()
#             sounds = tuple(i for i in temp[2:])
#             line = (temp[0], int(temp[1]), sounds)
#             all.add(line)
#     for element in all:
#         for i in element[2:]:
#             a = tuple(i)
#         if element[0] in dict_keyname.keys() and element[1] >= 1:
#             dict_keyname[element[0]].add(a)
#         else:
#             dict_keyname[element[0]] = set()
#             dict_keyname[element[0]].add(a)
#     return dict_keyname
#
#
# def dict_invert(lst_dict):
#     """
#     (list or dict) -> set
#
#     Return dictionary with keys - numbers of pronunciation of the word
#     input(dict): {'A.': {('EY1',)}, 'A': {('AH0', 'F', 'AO1', 'R', 'T'),
#                  ('EY1', 'F', 'AO1', 'R', 'T'), ('EY1', 'G', 'AO1', 'R', 'T')}}
#
#     input(list): ('A', 1, ['AH0']), ('A.', 1, ['EY1']), ('A', 2, ['EY1']),
#                   ('A42128', 1, ['EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W',
#                   'AH1', 'N', 'T', 'UW1', 'EY1', 'T']), ('AAA', 1, ['T', 'R',
#                   'IH2', 'P', 'AH0', 'L', 'EY1']), ('AABERG', 1, ['AA1', 'B',
#                   'ER0', 'G'])]
#
#     output: {3: {('A', ('AH0', 'F', 'AO1', 'R', 'T')),
#             ('A', ('EY1', 'G', 'AO1', 'R', 'T')),
#             ('A', ('EY1', 'F', 'AO1', 'R', 'T'))},
#             1: {('A.', ('EY1',))}}
#
#     >>> print("Done")
#     Done
#     """
#     new_dict = {}
#     if type(lst_dict) == dict:
#         for key, val in lst_dict.items():
#             num_val = len(val)
#             for i in range(1, 6):
#                 if num_val == i:
#                     if i not in new_dict.keys():
#                         new_dict[i] = set()
#                     for j in val:
#                         new_dict[i].add((key, j))
#     elif type(lst_dict) == list:
#         lst_dict = sorted(lst_dict)
#         for i in range(1, 6):
#             new_dict[i] = set()
#         check = 0
#         for i in range(len(lst_dict)):
#             if check == 0:
#                 lst = []
#                 while lst_dict[i] != lst_dict[-1] and \
#                         lst_dict[i][0] == lst_dict[i + 1][0]:
#                     check += 1
#                     lst.append(lst_dict[i])
#                     i += 1
#                 lst.append(lst_dict[i])
#                 for k in lst:
#                     new_dict[len(lst)].add((k[0], tuple(k[2])))
#             else:
#                 check -= 1
#     return new_dict
#
#
# print(dict_invert())



# n = int(input())
#
# com = int(input())
# for i in range(com):
#     lst = list(lambda x: x for x in input.strip().split())
# print(lst)
#

s = list(map(int, input().split()))
print(s)