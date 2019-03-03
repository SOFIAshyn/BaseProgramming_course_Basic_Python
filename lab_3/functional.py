lst = [1, 2, 3, -1, -2]
print(list(filter(lambda x: x% 2 ==0, lst)))
print(pow(len(list(filter(lambda x: x% 2 ==0, lst))), 2))
