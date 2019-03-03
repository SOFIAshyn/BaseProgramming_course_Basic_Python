import random

def binary_search(el, lst):
    left = 0
    right = len(lst)
    middle = (left + right) // 2
    middle_el = lst[middle]

    while left <= right:
        if middle_el == el:
            return el
        if middle_el > el:
            right = middle + 1
        elif middle_el < el:
            left = middle - 1
    return -1

def bin_search(n):
    min_in = 0
    max_in = len(new_lst)

    val = 53

    while True:
        new_index = (max_in + min_in) // 2

        if new_lst[new_index] == val and new_lst[new_index] == val and new_lst[new_index] == val:
            print("detected")
            break
        if val < new_lst[new_index]:
            max_in = new_index
        else:
            max_in = new_index

        if min_in == max_in - 1:
            print("not detected")
            break


p = 0.1
lst = list(range(1000))

new_lst = []

for el in lst:
    if random.uniform(0, 1) <= p:
        new_lst.append(el)

print(len(new_lst))


# c - codechef - begginer - atm (example) - tipical tasks for c
# codeforces
