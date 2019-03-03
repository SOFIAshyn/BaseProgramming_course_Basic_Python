import matplot.pyplot as plt
import time


def linearFunc(el, user_lst):
    iter_max = 1000
    iter_num = 100
    x = []
    y = []
    for n in range(1, iter_max + 2):
        each_time = []
        for each in range(1, iter_num + 2):
            start = time.time()
            linearsearch(el, user_lst)
            each_time.append(time.time() - start)
        x.append(len(user_lst))
        y.append(sum(each_time)/len(each_time))
    plt.plt(x, y)
    plt.show()



def linearsearch(el, user_lst):
    for i in user_lst:
        if i == el:
            return True
    return False
