from search import binarysearch, linearsearch
from norm import mergesort
import random
import os


def main(user_lst):
    linearsearch.linearFunc(user_lst)
    which_sort = input("Enter 'M' if you want to sort your list \
with merge sort. If you press something else it will be a random \
sorting algorithm")
    if which_sort == "M":
        sorted_user_lst = mergesort.mergesort(user_lst)
    else:
        all_sort = os.listdir(path=".")
        print(all_sort)
        random.shuffle(all_sort)
        one_file = random.choice(all_sort)
        sorted_user_lst = eval("one_file + '.' + one_file + '(' + user_lst + ')'")
    binarysearch.binaryFunc(sorted_user_lst)
