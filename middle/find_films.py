def find_films(path):
    """
    (str) -> set
    :return:
    """
    file = open(path, "r")
    data_set = {}
    lst = []
    for line in file:
        lst.append(line.split('\t'))
    lst = lst[1:]
    for i in range(len(lst)):
        lst[i][1] = float(lst[i][1])
        lst[i][2] = int(lst[i][2].replace(r'\n', ''))
        lst[i] = tuple(lst[i])
    data_set = set(lst)
    file.close()
    return data_set


def votes_dict(lines_set, num_v):
    dict = {}
    for el in lines_set:
        if el[2] > num_v:
            dict[el[0]] = (el[1], el[2])
    return dict


def films_id(n, dict_votes):
    """
    Return n films with highest rating
    :param n:
    :param dict_votes:
    :return:
    """
    lst = list(dict_votes.items())[:n]
    lst.sort(key=lambda x: x[1][0], reverse=True)
    rating_set = set(lst)
    return rating_set


def write_films_id(set_films_id):
    file = open("ready", "w+")
    file.write("tconst")
    for el in set_films_id:
        file.write(el[0] + '\n')
    file.close()
    return None


def find_films_id(num_v, n):
    lines_set = find_films("data2.tsv")
    dict_votes = votes_dict(lines_set, num_v)
    set_films_id = films_id(n, dict_votes)
    write_films_id(set_films_id)


if __name__ == "__main__":
    while True:
        num_v = input("Enter min number of votes: ")
        if num_v.isalnum():
            num_v = int(num_v)
            break
    while True:
        n = input("Enter number of films for rating table: ")
        if n.isalnum():
            n = int(n)
            break
    main(num_v, n)
