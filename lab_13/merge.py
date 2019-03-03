import random

# def merge(L1, L2):
#     """ (list, list) -> list
#     Merge sorted lists L1 and L2 into a new list and return that new list.
#     >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
#     [1, 1, 2, 3, 4, 5, 6, 7]
#     """
#     newL = []
#     i1, i2 = 0, 0
#     # For each pair of items L1[i1] and L2[i2], copy the smaller into newL.
#     while i1 != len(L1) and i2 != len(L2):
#         if L1[i1] <= L2[i2]:
#             newL.append(L1[i1])
#             i1 += 1
#         else:
#             newL.append(L2[i2])
#             i2 += 1
#     # Gather any leftover items from the two sections.
#     # Note that one of them will be empty because of the loop condition.
#     newL.extend(L1[i1:])
#     newL.extend(L2[i2:])
#     return newL

def merge(lst, start1, start2, end):



def call_merge(lst):
    n = len(lst)
    step = 1
    while(step < n):
        for start1 in range(0, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            merge(lst, start1, start2, end)
        step *= 2



if __name__ == "__main__":
    import doctest
    doctest.testmod()

    lst1 = [i for i in range(1, 100)]
    random.shuffle(lst1)
    print(call_merge(lst1))