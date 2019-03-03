import random
import matplotlib.pyplot as plt
import time

x = []
y = []
times = []
lst = [1, 4, 12, 13, 45, 2]


def bogosort():
    while True:
        print(lst)
        start = time.time()
        if lst == sorted(lst):
            print("Here is sorted list: ", lst)
            break
        times.append(time.time() - start)
        random.shuffle(lst)
        x.append(len(times))
        y.append(sum(times) / len(times))
    plt.title("BogoSort")
    plt.xlabel("Which time we are checking")
    plt.ylabel("Was it slow or quick?")
    plt.plot(x, y, label="bogosort")
    plt.show()
