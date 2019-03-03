import matplotlib.pyplot as plt
import time
import random


def binary_search(val, lst):
    left = 0
    right = len(lst) - 1
    while left <= right:
        middle = (left + right) // 2
        middle_el = lst[middle]
        if middle_el == val:
            return True
        if val > middle_el:
            left = middle + 1
        elif val < middle_el:
            right = middle - 1
    return -1

# val = 90
# lst = [i for i in range(1, 10)]
# print(binary_search(val, lst))

if __name__ == "__main__":
    iter_num = 1000
    iter_max = 1000
    x = []
    y = []
    for n in range(1, iter_max + 1):
        times = []
        for i in range(1, iter_num + 1):
            lst = list(range(n))
            val = random.randint(0, n - 1)
            start = time.time()
            binary_search(val, lst)
            times.append(time.time() - start)
        x.append(n)
        y.append(sum(times) / len(times))
    plt.plot(x, y)
    plt.show()