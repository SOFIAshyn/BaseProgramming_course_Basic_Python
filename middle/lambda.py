print(set(filter(lambda x: x < 10000, [x**y + y**x for x in range(2, 100) for y in range(2, 100)])))


# import collections
# >>> a = collections.Counter('abracadabra').most_common(3)
# >>> a
# [('a', 5), ('b', 2), ('r', 2)]
