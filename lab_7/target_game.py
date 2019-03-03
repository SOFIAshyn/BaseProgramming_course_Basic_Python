import random
import urllib.request

def generate_grid():
    """
    () -> list(list)

    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    field = []
    three_lst = []
    for three_let in range(0, 3):
        three_lst = []
        for i in range(0, 3):
            three_lst.append(chr(random.randint(97, 122)))
        field.append(three_lst)
    return field


def get_words(f, letters):
    """
    (str, list) -> list()

    Reads the file f. Checks the words with rules and returns a list of words.
    """
    # lettrs = []
    # okay = True
    # words = []
    # nline = ''
    # with open(f, 'r') as vocabulary:
    #     for line in vocabulary.readlines():
    #         nline = line.replace("\n", "").lower()
    #         if 4 <= len(nline) <= 9 and letters[4] in nline:
    #             lettrs = list(nline)
    #             for lettr in lettrs:
    #                 if lettr not in letters:
    #                     okay = False
    #                     break
    #                 else:
    #                     okay = True
    #             if okay is True:
    #                 words.append(nline)
    #
    # lettrs = copy.copy(letters)
    # nwords = []
    # okay = True
    # for word in words[::1]:
    #     lettrs = copy.copy(letters)
    #     for letter in word:
    #         if letter in lettrs:
    #             lettrs[lettrs.index(letter)] = '0'
    #         else:
    #             okay = False
    #             break
    #     if okay is True:
    #         nwords.append(word)
    #     okay = True
    #
    # unique = True
    # words = []
    # for word in nwords:
    #     if nwords.count(word) > 1:
    #         nwords.remove(word)
    # nwords.sort()
    # return nwords
    res = []
    cort_letters = []
    our_letters = []
    res = []
    f = open(f, 'r')
    for line in f:
        line = line.replace("\n", "").strip().lower()
        if 4 <= len(line) <= 9:
            if letters[4] in line:
                count = 0
                for each_letter in line:
                    if each_letter in letters:
                        count += 1
                if count == len(line):
                    our_letters.append(line)
    f.close()
    for each_word in our_letters:
        count_let = 0
        for each_letter in each_word:
            if each_word.count(each_letter) <= letters.count(each_letter):
                count_let += 1
            if count_let == len(each_word):
                res.append(each_word)
    for each in res:
        if res.count(each) > 1:
            res.remove(each)
    return sorted(res)


def get_user_words():
    """
    () -> list

    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = []
    while True:
        try:
            user_input = input()
            user_words.append(user_input)
            if user_input == "\x04":
                return user_words
        except EOFError:
            return user_words


def get_pure_user_words(user_words, letters, words_from_dict):
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    checked_user_words = []
    for each_user_word in user_words:
        if 4 <= len(each_user_word) <= 9:
            if letters[4] in each_user_word:
                count = 0
                for each_user_let in each_user_word:
                    if each_user_let in letters:
                        count += 1
                if count == len(each_user_word):
                    checked_user_words.append(each_user_word)
    for each_word in checked_user_words:
        count_let = 0
        if each_word in words_from_dict:
            checked_user_words.remove(each_word)
    for each_word in checked_user_words:
        coun_me = 0
        for each_let in each_word:
            if each_word.count(each_let) <= letters.count(each_word):
                count_me += 1
        if count_me == len(each_word):
            checked_user_words.remove(each_word)
    return (checked_user_words)


# checked_user_words = []
#     for each_user_word in user_words:
#         if 4 <= len(each_user_word) <= 9:
#             if letters[4] in each_user_word:
#                 count = 0
#                 for each_user_let in each_user_word:
#                     if each_user_let in letters:
#                         count += 1
#                 if count == len(each_user_word):
#                     checked_user_words.append(each_user_word)
#     for each_word in checked_user_words:
#         count_let = 0
#         if each_word in words_from_dict:
#             checked_user_words.remove(each_word)
#     return (checked_user_words)


def results():
    prop_words = []
    new_words = []
    generated_lst = generate_grid()
    print(generated_lst)
    user_words = get_user_words()
    en = "en.txt"
    generated_lst = generated_lst[0] + generated_lst[1] + generated_lst[2]
    generated_lst = [el for el in 'vhtdsrael']
    get_words_val  = get_words(en, generated_lst)
    correct_val = get_pure_user_words(user_words, generated_lst,
    get_words_val)
    correct_val_len = len(get_pure_user_words(user_words, generated_lst, get_words_val))
    all_words = sorted(get_words_val + correct_val)
    for each_dic_word in get_words_val:
        if each_dic_word not in correct_val:
            prop_words.append(each_dic_word)
    for each_user_word in correct_val:
        if each_user_word not in get_words_val:
            new_words.append(each_user_word)
    print()
    # print(correct_val_len)
    # print()
    print(all_words)
    print()
    print(prop_words)
    # print()
    # print(new_words)
    # print(get_words_val)
    # print(len(get_words_val))

results()

import doctest
doctest.testmod()
# generated_lst = generate_grid()
#
# print(generated_lst)
# generated_lst = generated_lst[0] + generated_lst[1] + generated_lst[2]
# generated_lst = [el for el in 'jniarnoah']
# user_words = get_user_words()
# en = open("en.txt", "r")
# get_words_val  = get_words(en, generated_lst)
# print(get_words_val)
# #print(get_words(en, [el for el in 'jniarnoah']))
# get_pure_user_words(user_words, generated_lst, get_words_val)
