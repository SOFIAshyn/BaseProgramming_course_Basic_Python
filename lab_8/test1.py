lst_dict = {'A.': {('EY1',)}, 'A': {('AH0', 'F', 'AO1', 'R', 'T'),
              ('EY1', 'F', 'AO1', 'R', 'T'), ('EY1', 'G', 'AO1',
              'R', 'T')}}


def dict_invert(lst_dict):
    """
    (list or dict) -> set

    Return dictionary with keys - numbers of pronunciationof the word
    input(dict): {'A.': {('EY1',)}, 'A': {('AH0', 'F', 'AO1', 'R', 'T'),
                  ('EY1', 'F', 'AO1', 'R', 'T'), ('EY1', 'G', 'AO1',
                  'R', 'T')}}

    input(list): [('A', 1, ['AH0']), ('A.', 1, ['EY1']), ('A', 2, ['EY1']),
                  ('A42128', 1, ['EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W',
                  'AH1', 'N', 'T', 'UW1', 'EY1', 'T']), ('AAA', 1, ['T', 'R',
                  'IH2', 'P', 'AH0', 'L', 'EY1']), ('AABERG', 1, ['AA1',
                  'B', 'ER0', 'G'])]

    output: {1: {('AABERG', ('AA1', 'B', 'ER0', 'G')),
            ('AAA', ('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1')),
            ('A.', ('EY1',)), ('A42128', ('EY1', 'F', 'AO1', 'R', 'T', 'UW1',
            'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T'))}, 2: {('A', ('AH0',)),
            ('A', ('EY1',))}, 3: set(), 4: set(), 5: set()}


    >>> len(dict_invert([('A', 1, ['AH0']), ('A.', 1, ['EY1']), ('A', 2, ['EY1']),('A42128', 1, ['EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T']), ('AAA', 1, ['T', 'R','IH2', 'P', 'AH0', 'L', 'EY1']), ('AABERG', 1, ['AA1', 'B', 'ER0', 'G'])]))
    2
    >>> len(dict_invert({'A.': {('EY1',)}, 'A': {('AH0', 'F', 'AO1', 'R', 'T'),('EY1', 'F', 'AO1', 'R', 'T'), ('EY1', 'G', 'AO1','R', 'T')}}))
    2
    """
    new_dict = {}
    if type(lst_dict) == dict:
        for key in lst_dict:
            new_dict[len(lst_dict[key])] = set()
        for key, val in lst_dict.items():
            num_val = len(val)
            for i in new_dict:
                if num_val == i:
                    for j in val:
                        new_dict[i].add((key, j))
    elif type(lst_dict) == list:
        lst_dict = sorted(lst_dict)
        for tup in lst_dict:
            new_dict[tup[1]] = set()
        check = 0
        for i in range(len(lst_dict)):
            if check == 0:
                lst = []
                while lst_dict[i] != lst_dict[-1] and\
                      lst_dict[i][0] == lst_dict[i+1][0]:
                    check += 1
                    lst.append(lst_dict[i])
                    i += 1
                lst.append(lst_dict[i])
                for k in lst:
                    new_dict[len(lst)].add((k[0], tuple(k[2])))
            else:
                check -= 1
    return new_dict

print((dict_invert([('A', 1, ['AH0']), ('A.', 1, ['EY1']), ('A', 2, ['EY1']), ('A42128', 1, ['EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T']), ('AAA', 1, ['T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1']), ('AABERG', 1, ['AA1', 'B', 'ER0', 'G'])])))
print((dict_invert({'AABERG': {('AA1', 'B', 'ER0', 'G')}, 'A.': {('EY1',)},
         'A': {('EY1',), ('AH0',)}, 'A42128': {('EY1', 'F', 'AO1',
         'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T')},
         'AAA': {('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1')}})))


# #print(dict_invert(sorted({'A.': {('EY1',)}, 'A': {('AH0', 'F', 'AO1', 'R', 'T'), ('EY1', 'F', 'AO1', 'R', 'T'), ('EY1', 'G', 'AO1', 'R', 'T')}})))
# print((dict_invert([('A', 1, ['AH0']), ('A.', 1, ['EY1']), ('A', 2, ['EY1']), ('A42128', 1, ['EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T']), ('AAA', 1, ['T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1']), ('AABERG', 1, ['AA1', 'B', 'ER0', 'G'])])))
