# import random
#
# def surname(sur_lst):
#     sur_file = open("surname.txt", "w")
#     for sur in sur_lst:
#         sur_file.write(sur, random.randint(1, 9))
#     sur_file.colse()
#
# lst = ["petryshyn", "ghghg", "kkkkkkk"]
# surname(lst)



# import random
#
# def surname_num(lst):
#     '''(list) -> None
#     Function for creating a list of surnames of students and random number between 1 and 9
#     >>> surname_num(["petryshyn", "nychai", "kosheliyk"])
#     printed to file:
#         petryshyn3
#         nychai1
#         kosheliyk7
#     '''
#     with open ("surname.txt", "w") as sur_file:
#         for student in lst:
#             print(student, random.randint(1, 9), end = "\n", sep = "", file = sur_file)
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
#     surname_num(["petryshyn", "nychai", "kosheliyk"])

import random


def surname_num(lst):
    '''(list) -> None
    Function for creating a list of surnames of students
    and random number between 1 and 9
    >>> surname_num(["petryshyn", "nychai", "kosheliyk"])
    printed to file:
        petryshyn3
        nychai1
        kosheliyk7
    '''
    with open("surnames.txt", "w") as sur_file:
        for student in lst:
            print(
                student, random.randint(1, 9),
                end="\n", sep='', file=sur_file)
