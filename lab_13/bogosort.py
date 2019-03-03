import random
import time
import matplotlib.pyplot as plt

def is_sorted(lst):
    for i, el in enumerate(lst):
        if

def bogo_sort(lst):
    while not is_sorted(lst):
        return False


if __name__ == "__main__":
    lst = [i for i in range(10)]
    random.shuffle(lst)
    print(bogo_sort(lst))

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
            bogo_sort(lst)
            times.append(time.time() - start)
        x.append(n)
        y.append(sum(times) / len(times))
    plt.plot(x, y)
    plt.show()