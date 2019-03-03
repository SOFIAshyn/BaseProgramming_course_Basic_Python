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
    my_file = open("data1.txt", "r")
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

#print(to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]]))

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
    for key in graph.keys():
        if key == edge[0]:
            if edge[1] in graph[key]:
                return graph
            else:
                graph[key].append(edge[1])
                graph[edge[1]].append(edge[0])
                key_here = True
    if key_here is False:
        graph[edge[0]] = [edge[1]]
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
        a += "\t\t" + str(key) + " -- {" + item_str.replace("[", "").replace("]", "").replace(",", "") + "};\n"
    a += "\t}"
    with open("graph.dot", "w") as f:
        f.write(a)

#convert_to_dot({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]})


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
