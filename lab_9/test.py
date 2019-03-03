#example output [(1, '.25-caliber-pistol'), (2, '.30-calibre-bullet')]

lst = ["	.25-caliber-pistol (1)		.30-calibre-bullet (2)".strip(),
	".32-caliber-pistol (1)		.357-magnum (15)".strip()]

k = [w.split("\t") for w in lst]
keywords = list(filter(lambda x: x != '', (x for x in [lst for lst in k])))
print(keywords, " dfghj")

#keywords = tuple(map(lambda w: w, [for lst1 in keywords[:-1] for w in lst1]))

#keywords = [map(int(w, " ")[1][1:-1]) for lst1 in keywords[:-1] for w in lst1 if w]

keywords = [(int(w.split()[1][1:-1]), w.split()[0])
            for lst1 in keywords[:-1] for w in lst1 if w]
# keywords =
#
# # for lst1 in keywords[:-1]:
# #     for w in lst1:
# #         if w:
# #             keywords = [(int(w.split()[1][1:-1]), w.split()[0])]
#
#
print(keywords)
#################################################

# f = open("text.txt", "r", encoding='utf-8', errors='ignore')
# data = f.readline()
# print(data)
# from_line = 3
# data = ""
# data = readline(f, start=item[from_line])
# print(data)
