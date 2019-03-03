def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    my_lst = []
    file_name = open(file_name, encoding="utf-8")
    text = file_name.readlines()
    lines = [list(map(int, line.split(","))) for line in text]
    # for each in text:
    #     my_key, my_val = map(int, each.split(","))
    #     my_lst.append([my_key, my_val])
    return (lines)

def to_edge_dict(edge_list):
    """
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [3, 2], 5: [1]}
    """
    my_dict = {}
    for each_lst in edge_list:
        for each_el in each_lst:
            if each_el not in my_dict.keys():
                my_dict[each_el] = []
    for each_lst in edge_list:
        for key in my_dict.keys():
            if key == each_lst[0]:
                my_dict[key].append(each_lst[1])
            elif key == each_lst[1]:
                my_dict[key].append(each_lst[0])
    return (my_dict)


def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> dict

    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    if edge[0] in graph.keys():
        for each_el in graph.values():
            if each_el == edge[1]:
                return True
            else:
                return False


def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (0, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    for key, val in graph.items():
        if key == edge[0] and (i == edge[1] for i in range(len(val))):
            print(graph)
        else:
            if edge[0] not in graph.keys():
                graph.keys().add(edge[0])
    print(graph)


def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    pass

def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    pass

def del_node(graph, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    pass

def convert_to_dot(graph):
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    """
    pass

edge_list = get_graph_from_file("data1.txt")
print(edge_list)
graph = to_edge_dict(edge_list)
add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
#
# import doctest
# doctest.testmod()
