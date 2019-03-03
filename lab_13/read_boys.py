def open_file(file_name):
    file = open(file_name, "r")
    dict_names = {}
    for line in file:
        lst = line.strip().split()
        if line[0].isalpha():
            dict_names[lst[0]] = int(lst[1].replace("(", "").replace(")", ""))
    file.close()
    return dict_names

def find_max(lst, max):
    i = max + 1
    while i != len(lst):
        if lst[i] > lst[max]:
            max = i
        i += 1
    return max


def linear_sort(dict):
    lst = list(dict.items())
    i = 0
    while (i != len(lst)):
        max = find_max(lst, i)
        lst[i], lst[max] = lst[max], lst[i]
        i += 1
    return lst



if __name__ == "__main__":
    import time

    dict_names = open_file("boy_names")
    print(open_file("boy_names"))
    #unsorted
    start = time.time()
    print("Max = ", linear_sort(dict_names))
    print("time of find popular = {:.7f}".format(time.time() - start))
