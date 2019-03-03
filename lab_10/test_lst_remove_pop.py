# a = int(input())
# n = set(map(int, input().split()))
# n_com = int(input())
#
# for i in range(n_com):
#     com, val = input().split()
#     if com == "remove":
#         n.remove(int(val))
#     elif com == "pop":
#         n.oop(int(val))
#     else:
#         n.discard(int(val))
# print(n)

def common_names(female_names, male_names):
    """
    (str, str) -> set

    Return set with names that is the same for males and females.
    """
    female_names = set(tuple(i for i in names_read(female_names)))
    male_names = set(tuple(i for i in names_read(male_names)))
    res = female_names.intersection(male_names)
    return res


def names_read(file_name):
    """
    (str) -> list

    Return list of names from inputed file
    """
    names = []
    f = open(file_name)
    for line in f.readlines():
        names.append(line.replace("\n", ""))
    return names

#print(names_read("female.txt"))
print(common_names("female.txt", "male.txt"))



# a = int(input())
# n = set(map(int, input().split()))
# n_com = int(input())
#
# for i in range(n_com):
#     com, val = input().split()
#     if com == "remove":
#         n.remove(int(val))
#     elif com == "pop":
#         n.oop(int(val))
#     else:
#         n.discard(int(val))
# print(n)

# def common_names(female_names, male_names):
#     """
#     (str, str) -> set
#
#     Return set with names that is the same for males and females.
#     """
#     #female_names = set(tuple(i for i in names_read(female_names)))
#     #male_names = set(tuple(i) for i in names_read(male_names)))
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
#     f = open(file_name, "r")
#     for line in f.readlines():
#         names.add(line[:-1])
#     f.close()
#     return names
#
# print(common_names("female.txt", "male.txt"))