import time

def binary_search(el, lst):
    left = 0
    right = len(lst)
    middle = (left + right) // 2
    middle_el = lst[middle]

    while left <= right:
        if middle_el == el:
            return middle, el
        if middle_el > el:
            right = middle - 1
        elif middle_el < el:
            left = middle + 1
    return -1


def linery_search(el, lst):
    for i, element in lst:
        if element == el:
            return i, el


if __name__ == "__main__":
    a = 2
    lst = [x for x in range(10)]

    start = time.time()
    print(a in lst)
    end = time.time()
    print("Work with our cycle {:.6f}".format(end - start))

    start = time.time()
    lst = set(lst)
    print(a in lst)
    end = time.time()
    print("Work with a set {:.6f}".format(end - start))

    start = time.time()
    print(linery_search(el, lst))
    end = time.time()
    print("Work with our linery_search {:.6f}".format(end - start))

    start = time.time()
    print(binary_search(el, lst))
    end = time.time()
    print("Work with our binary_search {:.6f}".format(end - start))

    all_words = {}

    text = open("text.txt", "r")
    words = text.split()

    for word in words:
        if word == word[::-1]
            if word not in all_words:
                all_words[word] = 0
            all_words[word] += 1

    most_common = sorted([(count, word) for word, count in all_words.items()], reverse = True)[:10]
    print(most_common)

    print(Counter(filter(lambda x: x == x[::-1], words)).most_common(10))


    lst = set(lst)
    print(a in lst)
    print(binary_search(a, lst))





    # anagram words

