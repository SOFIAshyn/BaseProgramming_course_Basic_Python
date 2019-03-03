# def common_names(female_names, male_names):
#     """
#     (str, str) -> set
#
#     Return set with names that is the same for males and females.
#     """
#     female_names = set(tuple(i for i in names_read(female_names)))
#     male_names = set(tuple(i for i in names_read(male_names)))
#     res = female_names.intersection(male_names)
#     return res
#
#
# def names_read(file_name):
#     """
#     (str) -> list
#
#     Return list of names from inputed file
#     """
#     names = []
#     f = open(file_name)
#     for line in f.readlines():
#         names.append(line.replace("\n", ""))
#     return names

def common_names(female_names, male_names):
    """
    (str, str) -> set

    Return set with names that is the same for males and females.

    >>> common_names(["Gary", "Very", "Kim"], ["Kim", "Lily"])
    {'Kim'}
    """
    female_names = set(i for i in female_names)
    male_names = set(i for i in male_names)
    res = female_names.intersection(male_names)
    return res


def names_read(file_name):
    """
    (str) -> list

    Return list of names from inputed file
    """
    names = []
    f = open(file_name, "r")
    for line in f.readlines():
        names.append(line[:-1])
    if 'Gale' in names:
        names.remove('Gale')
    f.close()
    return len(names)

print(names_read("female.txt"))
# a = names_read("female.txt")
# b = names_read("male.txt")
# print(common_names(a, b))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
