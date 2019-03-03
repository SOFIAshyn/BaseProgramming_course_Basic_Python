# # # def dict_reader_tuple(file_dict):
# # #     """
# # #     (str) -> set
# # #
# # #     Return set of lines from inputed file (name, number of pronunsiation,
# # #     sounds)
# # #     output: {('A.', 1, ('EY1',)), ('A', 2, ('EY1', 'F', 'AO1', 'R', 'T')),
# # #     ('A', 1, ('AH0', 'F', 'AO1', 'R', 'T'))}
# # #     """
# # #     all = set()
# # #     with open(file_dict, "r") as file:
# # #         for line in file.readlines():
# # #             line = line.replace("\n", "")
# # #             temp = line.split()
# # #             sounds = tuple(i for i in temp[2:])
# # #             line = (temp[0], int(temp[1]), sounds)
# # #             all.add(line)
# # #     return all
# #
# # def dict_reader_tuple(file_dict):
# #     """
# #     (str) -> set
# #
# #     Return set of lines from inputed file (name, number of pronunsiation,
# #     sounds)
# #     output: [('A', 1, ['AH0']), ('A.', 1, ['EY1']), ('A', 2, ['EY1']),
# #     ('A42128', 1, ['EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T',
# #     'UW1', 'EY1', 'T']), ('AAA', 1, ['T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1']),
# #     ('AABERG', 1, ['AA1', 'B', 'ER0', 'G'])]
# #     """
# #     all = list()
# #     with open(file_dict, "r") as file:
# #         for line in file.readlines():
# #             line = line.replace("\n", "")
# #             temp = line.split()
# #             sounds = list(i for i in temp[2:])
# #             line = (temp[0], int(temp[1]), sounds)
# #             all.append(line)
# #     return all
# #
# # def dict_reader_dict(file_dict):
# #     """
# #     (set) -> dict
# #
# #     Return dictionary with name key, where items is sounds of the word.
# #
# #     output: {'A.': {('EY1',)}, 'A': {('AH0', 'F', 'AO1', 'R', 'T'),
# #           ('EY1', 'F', 'AO1', 'R', 'T'), ('EY1', 'G', 'AO1', 'R', 'T')}}
# #     """
# #     all = set()
# #     dict_keyname = {}
# #     with open(file_dict, "r") as file:
# #         for line in file.readlines():
# #             line = line.replace("\n", "")
# #             temp = line.split()
# #             sounds = tuple(i for i in temp[2:])
# #             line = (temp[0], int(temp[1]), sounds)
# #             all.add(line)
# #     for element in all:
# #         for i in element[2:]:
# #             a = tuple(i)
# #         if element[0] in dict_keyname.keys() and element[1] >= 1:
# #             dict_keyname[element[0]].add(a)
# #         else:
# #             dict_keyname[element[0]] = set()
# #             dict_keyname[element[0]].add(a)
# #     return dict_keyname
# #
# #
# # # def dict_invert(dict):
# # #     """
# # #     (dict) -> set
# # #
# # #     Return dictionary with keys - numbers of pronunciationof the word
# # #     input: {('A.', 1, ('EY1',)), ('A', 2, ('EY1', 'F', 'AO1', 'R', 'T')),
# # #             ('A', 1, ('AH0', 'F', 'AO1', 'R', 'T'))}
# # #     output: {1: {('A', ('AH0', 'F', 'AO1', 'R', 'T')), ('A.', ('EY1',))},
# # #           2: {('A', ('EY1', 'F', 'AO1', 'R', 'T'))}}
# # #     """
# # #     dict_keyname = {}
# # #     for element in dict:
# # #         for i in element[2:]:
# # #             a = tuple(i)
# # #         if element[0] in dict_keyname.keys() and element[1] >= 1:
# # #             dict_keyname[element[0]].add(a)
# # #         else:
# # #             dict_keyname[element[0]] = set()
# # #             dict_keyname[element[0]].add(a)
# # #     new_dict = {}
# # #     for key, val in dict_keyname.items():
# # #         num_val = len(val)
# # #         for i in range(1, 6):
# # #             if num_val == i:
# # #                 if i not in new_dict.keys():
# # #                     new_dict[i] = set()
# # #                 for j in val:
# # #                     new_dict[i].add((key, j))
# # #     return new_dict
# #
# #
# # def dict_invert(lst_dict):
# #     """
# #     (list or dict) -> set
# #
# #     Return dictionary with keys - numbers of pronunciationof the word
# #     input(dict): {'A.': {('EY1',)}, 'A': {('AH0', 'F', 'AO1', 'R', 'T'),
# #                  ('EY1', 'F', 'AO1', 'R', 'T'), ('EY1', 'G', 'AO1', 'R', 'T')}}
# #
# #     input(list): ('A', 1, ['AH0']), ('A.', 1, ['EY1']), ('A', 2, ['EY1']),
# #                   ('A42128', 1, ['EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W',
# #                   'AH1', 'N', 'T', 'UW1', 'EY1', 'T']), ('AAA', 1, ['T', 'R',
# #                   'IH2', 'P', 'AH0', 'L', 'EY1']), ('AABERG', 1, ['AA1', 'B',
# #                   'ER0', 'G'])]
# #
# #     output: {3: {('A', ('AH0', 'F', 'AO1', 'R', 'T')),
# #             ('A', ('EY1', 'G', 'AO1', 'R', 'T')),
# #             ('A', ('EY1', 'F', 'AO1', 'R', 'T'))},
# #             1: {('A.', ('EY1',))}}
# #     """
# #     new_dict = {}
# #     if type(lst_dict) == dict:
# #         for key, val in lst_dict.items():
# #             num_val = len(val)
# #             for i in range(1, 6):
# #                 if num_val == i:
# #                     if i not in new_dict.keys():
# #                         new_dict[i] = set()
# #                     for j in val:
# #                         new_dict[i].add((key, j))
# #     elif type(lst_dict) == list:
# #         lst_dict = sorted(lst_dict)
# #         for i in range(1, 6):
# #             new_dict[i] = set()
# #         check = 0
# #         for i in range(len(lst_dict)):
# #             if check == 0:
# #                 lst = []
# #                 while lst_dict[i] != lst_dict[-1] and\
# #                 lst_dict[i][0] == lst_dict[i+1][0]:
# #                     check += 1
# #                     lst.append(lst_dict[i])
# #                     i += 1
# #                 lst.append(lst_dict[i])
# #                 for k in lst:
# #                     new_dict[len(lst)].add((k[0], tuple(k[2])))
# #             else:
# #                 check -= 1
# #     return new_dict
# #
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
#     Return dictionary with keys - numbers of pronunciationof the word
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
#                 while lst_dict[i] != lst_dict[-1] and\
#                       lst_dict[i][0] == lst_dict[i+1][0]:
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
# #
# #
# # # print(dict_reader_tuple("cmudict"))
# # # dict_reader_dict(dict_reader_tuple("cmudict"))
# #a = dict_reader_dict("cmudict")
# a = dict_reader_tuple("cmudict")
# #print(dict_reader_dict("cmudict"))
# print(dict_invert(a))
# # #print(a)




# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.


def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    my_file = open(file_name, "r")
    graph = []
    graph = list(list(map(int, line.split(","))) for line in my_file)
    my_file.close()
    return graph


def to_edge_dict(edge_list):
    """
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    dict = {}
    lst_set = []
    for line_lst in edge_list:
        lst_set += line_lst
    lst_set = set(lst_set)
    for i in lst_set:
        dict[i] = []
    for key in dict.keys():
        for line_lst in edge_list:
            if key == line_lst[0]:
                if line_lst[1] not in dict[key]:
                    dict[key].append(line_lst[1])
            elif key == line_lst[1]:
                if line_lst[0] not in dict[key]:
                    dict[key].append(line_lst[0])
    for each in dict.values():
        each.sort()
    return dict


def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> dict

    Return True if graph contains a given edge and False otherwise.
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]},\
    (3, 1))
    False
    """
    check = False
    for key in graph.keys():
        if key == edge[0]:
            for val in graph[key]:
                if val == edge[1]:
                    check = True
    return check


def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    key_here = False
    if edge[0] not in graph.keys():
        graph[edge[0]] = []
    if edge[1] not in graph.keys():
        graph[edge[1]] = []
    for key in graph.keys():
        if key == edge[0]:
            graph[key].append(edge[1])
        elif key == edge[1]:
            graph[key].append(edge[0])
    # if edge[0] not in graph.keys():
    #     graph[edge[0]] = []
    # for key in graph.keys():
    #     if key == edge[0]:
    #         if edge[1] in graph[key]:
    #             return graph
    #         else:
    #             graph[key].append(edge[1])
    #             graph[edge[1]].append(edge[0])
    #             key_here = True
    # if key_here is False:
    #     graph[edge[0]] = [edge[1]]
    return graph


def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    key_here = False
    for key in graph.keys():
        if key == edge[0]:
            if edge[1] in graph[key]:
                graph[key].remove(edge[1])
                graph[edge[1]].remove(edge[0])
    return graph


def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node not in graph.keys():
        graph[node] = []
    return graph


def del_node(graph, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph.keys():
        del graph[node]
    for val_lst in graph.values():
        if node in val_lst:
            val_lst.remove(node)
    return(graph)


def convert_to_dot(graph):
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    """
    a = "graph{\n"
    item_str = ""
    for key, item in graph.items():
        item_str = ""
        for el in item:
            item_str += str(el) + " "
        a += "\t\t" + str(key) + " -- {" + item_str.replace("[", "").\
        replace("]", "").replace(",", "") + "};\n"
    a += "\t}"
    with open("graph.dot", "w") as f:
        f.write(a)

# # print(dict_reader_tuple("cmudict"))
# # dict_reader_dict(dict_reader_tuple("cmudict"))
#a = dict_reader_dict("cmudict")
#a = dict_reader_tuple("cmudict")
#print(dict_reader_dict("cmudict"))
#print(dict_invert(a))
# #print(a)
print(add_node({1: [2], 2: [1]}, 1))
print(add_node({1: [2], 2: [1]}, 4))
print(add_node({1: [2], 3: [1]}, 2))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
