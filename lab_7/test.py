# # song_titles = ['Я на небі був', 'Той день', 'Мало мені', 'Сосни', 'Кавачай',
# #             'Відпусти', 'Африка', 'Поясни', 'Фіалки мої', 'Коли тебе нема', 'Етюд']
# # length_songs = ['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24',
# #                 '3.39', '3.43', '3.17', 2.21]
# #
# # if filter(lambda i: isinstance(i, str) is False, song_titles):
# #     print("fgh")
# #
# # for i in length_songs:
# #     for j in song_titles:
# #         if (isinstance(i, str) is False or isinstance(j, str) is False):
# #             print("dfgfo;kp'itsrastg.hil/j")
#
#
# def song_length(x):
#     """(zip) -> int
#
#     Return the time of the song
#     """
#     return x[1]
#
#
# def title_length(x):
#     """(zip) -> int
#
#     Return lenght of the name of the song_length
#     """
#     return len(x[0])
#
#
# def last_word(x):
#     """(zip) -> str
#
#     Return last word of the name of the song to compare
#     """
#     words = x[0].split(" ")
#     return words[-1]
#
#
# def sort_songs(song_titles, length_songs, key):
#     """(list, list, function) -> list
#
#     Return list of sorted values due to the key
#
#     >>> sort_songs(song_titles, length_songs, song_length)
#     [('Етюд', '2.21'), ('Коли тебе нема', '3.17'), ('Я на небі був', '3.19'),\
#  ('Поясни', '3.39'), ('Фіалки мої', '3.43'), ('Відпусти', '3.52'),\
#  ('Той день', '3.58'), ('Африка', '4.24'), ('Сосни', '4.31'),\
#  ('Кавачай', '4.39'), ('Мало мені', '5.06')]
#
#     >>> sort_songs(song_titles, length_songs, title_length)
#     [('Етюд', '2.21'), ('Сосни', '4.31'), ('Африка', '4.24'),\
#  ('Поясни', '3.39'), ('Кавачай', '4.39'), ('Той день', '3.58'),\
#  ('Відпусти', '3.52'), ('Мало мені', '5.06'), ('Фіалки мої', '3.43'),\
#  ('Я на небі був', '3.19'), ('Коли тебе нема', '3.17')]
#
#     >>> sort_songs(song_titles, length_songs, last_word)
#     [('Африка', '4.24'), ('Відпусти', '3.52'), ('Етюд', '2.21'),\
#  ('Кавачай', '4.39'), ('Поясни', '3.39'), ('Сосни', '4.31'),\
#  ('Я на небі був', '3.19'), ('Той день', '3.58'), ('Мало мені', '5.06'),\
#  ('Фіалки мої', '3.43'), ('Коли тебе нема', '3.17')]
#     """
#     if len(song_titles) != len(length_songs):
#         return None
#     for i in length_songs:
#         for j in song_titles:
#             if isinstance(i, str) is False or isinstance(j, str) is False:
#                 return None
#             else:
#                 x = zip(song_titles, length_songs)
#                 return(sorted(x, key=key))
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()


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
    """() -> list
    Returns a list with these words.
    Gets words from user input.
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
    """(list, list, list) -> list

    Return list of words thst are not in dictionary.
    Words are firstly checked with rules.
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
    return (checked_user_words)


def results():
    """
    () -> ()

    Prints list of letters, correct words entered by user, all
    words, words that user missed, words that user added.
    """
    prop_words = []
    new_words = []
    generated_lst = generate_grid()
    print(generated_lst)
    user_words = get_user_words()
    en = open("en.txt", "r")
    generated_lst = generated_lst[0] + generated_lst[1] + generated_lst[2]
    get_words_val  = get_words(en, generated_lst)
    correct_val = get_pure_user_words(user_words, generated_lst,
                                        get_words_val)
    correct_val_len = len(get_pure_user_words(user_words, generated_lst,\
    get_words_val))
    all_words = sorted(get_words_val + correct_val)
    for each_dic_word in get_words_val:
        if each_dic_word not in correct_val:
            prop_words.append(each_dic_word)
    for each_user_word in correct_val:
        if each_user_word not in get_words_val:
            new_words.append(each_user_word)
    print()
    print(correct_val_len)
    print()
    print(all_words)
    print()
    print(prop_words)
    print()
    print(new_words)

result()
