# def calculate(numbers):
#     """
#     (list) -> tuple
#
#     Return list of numbers, lenght of list, sum of each element, lowest element,
#     highest element, mean number, mediana.
#
#     >>> calculate([5, 7, 3, 2])
#     ([5, 7, 3, 2], 4, 17, 2, 7, 4.25)
#     """
#     # if len(numbers) % 2 != 0:
#     #     mediana = mediana = sorted(numbers)[len(numbers)//2 + 1]
#     # else:
#     #     mediana = (sorted(numbers)[len(numbers)//2] +
#     #                 sorted(numbers)[len(numbers)//2 + 1])/2
#     # str = "numbers: " + numbers + "\ncount = " + len(numbers) + "sum = " %d
#     #             "lowest = %d highest = %d mean = " % (numbers, len(numbers), sum(numbers), min(numbers), max(numbers),
#     #             sum(numbers)/len(numbers)))
#     # return str
#     return(numbers, len(numbers), sum(numbers), min(numbers), max(numbers),
#             sum(numbers)/len(numbers))
#
# #print(calculate([5, 7, 3, 2]))
#
# input_num = []
# try:
#     while True:
#         user_input = input("enter a number or Enter to finish: ")
#         input_num.append(int(user_input))
# except ValueError as err:
#     res = calculate(input_num)
#     print("numbers: ", res[0])
#     print("numbers: ", res[0])
# # user_input = input("enter a number or Enter to finish: ")
# #
# # while user_input:
# #     input_num.append(int(user_input))
# #     user_input = input("enter a number or Enter to finish: ")
#

#
# # import doctest
# # doctest.testmod()
# # print("count = {} sum = {} lowest = {} highest = {} mean = {}".format(input_num[1], input_num[2], input_num[3], input_num[4], input_num[5]))
#
#
#
# #print("count = %d sum = %d lowest = %d highest = %d mean = %f" % (input_num[i] for i in range(1, 5)))
def calculate(numbers):
    """
    (list) -> tuple

    Return list of numbers, lenght of list, sum of each element, lowest element,
    highest element, mean number, mediana.

    >>> calculate([5, 7, 3, 2])
    ([5, 7, 3, 2], 4, 17, 2, 7, 4.25)
    """
    if len(numbers) % 2 != 0:
        print([len(numbers)//2 + 1])
        mediana = sorted(numbers)[len(numbers)//2]
    else:
        mediana = (sorted(numbers)[len(numbers)//2] +
                    sorted(numbers)[len(numbers)//2 - 1])/2
    return (numbers, len(numbers), sum(numbers), min(numbers), max(numbers), sum(numbers)/len(numbers), mediana)


input_num = []
if __name__ == "__main__":
    try:
        while True:
            user_input = input("enter a number or Enter to finish: ")
            input_num.append(int(user_input))
    except ValueError as err:
        print(err)
    cal_input = calculate([5, 4, 1, 8, 5, 2])
    print("numbers: ", cal_input[0])
    print("count = %d sum = %d lowest = %d highest = %d" %
               (cal_input[1], cal_input[2], cal_input[3], cal_input[4]),
                "mean = ", cal_input[5], "mediana = ", cal_input[6])
    # print("count = %d sum = %d lowest = %d highest = %d mean = %17.15f mediana = %d" %
    #        (cal_input[1], cal_input[2], cal_input[3], cal_input[4], cal_input[5], cal_input[6]))

print(calculate([5, 7, 3, 2]))
