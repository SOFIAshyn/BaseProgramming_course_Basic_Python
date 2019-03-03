def file_read(file_name):
    file = open(file_name, "r")
    dictionary = {}
    for line in file:
        lst = line.strip().split()
        if line[0].isalpha():
            dictionary[lst[0]] = int(lst[1].replace("(", "").replace(")", ""))
    file.close()
    return dictionary

import collections
def work_with_names(dic):
    def find_popular(dic):
        lst = list(dic.items())
        print(lst)
        lst.sort(key=lambda el: el[1])
        return lst

    def only_one(lst):
        lst_one = []
        lst = lst[::-1]
        for el in lst:
            if el[1] == 1:
                lst_one.append(el)
        return lst_one

    def letter_names(dic):
        """
        first letter
        :param dic:
        :return:
        """
        lst_first_letter = []
        for el in dic.keys():
            lst_first_letter.append(el[0])
        dict_f_l = {}
        for el in lst_first_letter:
            if el not in dict_f_l:
                dict_f_l[el] = 0
            dict_f_l[el] += 1
        return dict_f_l

    def count_one_letter_names(dic_all):
        """
        the same letter numbers
        :param dic_all:
        :return:
        """
        dic_first_all = {}
        for el, val in dic_all.items():
            if el not in dic_first_all:
                dic_first_all[el] = 0
            dic_first_all[el] += val
        return dic_first_all

    def attach_all_lett(dic_let, dic_all):
        combination = []
        for key1 in dic_let:
            for key2 in dic_all:
                if key1 == key2[0]:
                    combination.append([key1, dic_let[key1], dic_all[key2]])
        return combination

    def filter_comb(lst):
        new_lst = []
        for i in range(len(lst) - 1):
            if lst[i][0] == lst[i+1][0]:
                lst[i+1][2] += lst[i][2]
            else:
                new_lst.append(lst[i])
        return (new_lst)


    lst_pop = find_popular(dic)
    lst_one = only_one(find_popular(dic))
    first = letter_names(file_read("boy_names"))
    second = count_one_letter_names(file_read("boy_names"))
    simularities = filter_comb(attach_all_lett(first, second))

    return lst_pop, lst_one, simularities


def main():
    lst = work_with_names(file_read("boy_names"))
    print("Top 10:", lst[0][:5])
    print("One : ", lst[1])
    print("One letter - number of names, one letter numbers of boys:\n", lst[2])

main()