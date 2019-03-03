# # ****************************************
# # Problem 7
# # ****************************************
# def convert_to_column(s):
#     """str -> str
#     Convert string to a column of words.
#     If argument is not a string function should return None.
#
#     >>> convert_to_column("Revenge is a dish that tastes best when served cold.")
#     revenge
#     is
#     a
#     dish
#     that
#     tastes
#     best
#     when
#     served
#     cold
#     >>> convert_to_column("Never hate your enemies. It affects your judgment.")
#     never
#     hate
#     your
#     enemies
#     it
#     affects
#     your
#     judgment
#     >>> convert_to_column(2015)
#     """
#     if type(s) == str:
#         new_s = ""
#         lst = s.split(" ")
#         for i in lst:
#             new_s += i.lower().replace(".", "").replace(",", "").replace("-", "") + "\n"
#         return (new_s)
#     else:
#         return None
#
# print(convert_to_column("Revenge is a dish that tastes best when served cold."))
#
# if __name__ == "__main__":
#   import doctest
#   print(doctest.testmod())

text = open('text.txt')

intmap = list(map(int, text.readline().strip('\n'))
intlist = list(intmap)

text.close()

print(intmap)
