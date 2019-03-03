"""
FIBONACHI WITH OLES'
"""

import sys
from functools import lru_cache

sys.setrecursionlimit(1000000000)
memory = {}

def fib(n):
    print("f({}) = f({})".format(n, n - 1, n - 2))
    if n <= 1:
        return 1
    if n not in memory:
        memory[n] = fib(n - 1) + fib(n - 2)
    return memory[n]


@lru_cache(maxsize=10000)
def old_fib(n):
    if n <= 1:
        return 1
    return old_fib(n - 1) + fib(n - 2)


# if __name__ == "__main__":
#     print(fib(100))
#     print(old_fib(50))

"""
ThE SECOND
"""
# import sys

# sys.setrecursionlimit(100000)

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n


def factorial_for(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac


# print(factorial(5))
# print(factorial_for(5))


"""
THE THIRD
"""

def factorial(n, depth=0):
    print(" "*depth, "factorial(",n,"):")
    if (n < 2):
        result = 1
    else:
        result = n*factorial(n-1,depth+1)
    print(" "*depth, "-->", result)
    return result

# print(factorial(5))

"""
THE FOURTH
"""

# lst = [3, 4, 5]
#
# import time
#
# the fastest
# st = time.time()
# lst += [6]
# print("first: ", time.time() - st)
#
# the slowest
# st = time.time()
# lst = lst + [6]
# print("second: ", time.time() - st)
#
# the second
# st = time.time()
# lst.append(6)
# print("third: ", time.time() - st)

"""
THE FIFTH
"""

def find_path(graph, start, end, path=[]):
    path += [start]
    print("path: ", path)
    if start == end:
        return path
    print("graph[start]: ", graph[start])
    if start not in graph:
        return None
    for node in graph[start]:
        print("graph: ", graph, 'node = ', node)
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    # return None

# dic = { 1: [ 2, 3 ],2: [ 3, 4 ],3: [ 4 ],4: [ 3 ],5: [ 6 ],6: [ 3 ] }
# print(dic)
# print(find_path(dic, 1, 4))


"""
SIX
"""

def to_begin(lst, el):
    return (lst, el, 0, len(lst))

def rec_bin_search(lst, el, left, right):
    if left >= right:
        return -1
    else:
        midle = (left + right) // 2
        mid_el = lst[midle]

        if mid_el == el:
            return midle
        elif mid_el < el:
            left = midle - 1
            return (rec_bin_search(lst, el, left, right))
        else:
            right = midle + 1
            return (rec_bin_search(lst, el, left, right))


# lst = [x for x in range(100)]
#
# lst, el, left, right = to_begin(lst, 5)
# print(rec_bin_search(lst, el, left, right))

"""
SEVEN
"""

# def power(a, n):
#     res = 1
#     for i in range(n):
#         res *= a
#     return res

#MINE

# def rec_power(a, n):
#     if n == 0:
#         return 1
#     else:
#         print("a * rec_power(", a, ", ",n - 1,") = ", a * rec_power(a, n - 1))
#         return a * rec_power(a, n - 1)

# ROMANYUKA

def rec_poer_rom(a, n):
    if n == 0:
        return 0
    else:
        factor = rec_bin_search(a,n//2)
        if factor % 2 == 1:
            return factor * factor
        else:
            return factor * factor * a



# print(power(2, 3))
# print(rec_power(2, 3))

"""
EIGHT
"""

def nsd(a, b):
    if a == b:
        return a
    else:
        if a > b:
            return nsd(a - b, b)
        else:
            return nsd(a, b - a)


def nsd_2(a, b):
    if a == b or b == 0:
        return a
    else:
        return nsd_2(b, a % b)

# print(nsd(3, 6))
# print(nsd_2(30, 6))

"""
NINE
"""











# module intertools
# dinamic programing
# counter