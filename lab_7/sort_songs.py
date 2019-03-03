def song_length(x):
    """(zip) -> int

    Return the time of the song
    """
    return x[1]


def title_length(x):
    """(zip) -> int

    Return lenght of the name of the song_length
    """
    return len(x[0])


def last_word(x):
    """(zip) -> str

    Return last word of the name of the song to compare
    """
    words = x[0].split(" ")
    return words[-1]


def sort_songs(song_titles, length_songs, key):
    """(list, list, function) -> list

    Return list of sorted values due to the key

    >>> sort_songs(['Я на небі був', 'Той день', 'Мало мені', 'Сосни',\
 'Кавачай', 'Відпусти', 'Африка', 'Поясни', 'Фіалки мої', 'Коли тебе нема',\
 'Етюд'], ['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39',\
 '3.43', '3.17', '2.21'], song_length)
    [('Етюд', '2.21'), ('Коли тебе нема', '3.17'), ('Я на небі був', '3.19'),\
 ('Поясни', '3.39'), ('Фіалки мої', '3.43'), ('Відпусти', '3.52'),\
 ('Той день', '3.58'), ('Африка', '4.24'), ('Сосни', '4.31'),\
 ('Кавачай', '4.39'), ('Мало мені', '5.06')]

 #    >>> sort_songs(song_titles, length_songs, title_length)
 #    [('Етюд', '2.21'), ('Сосни', '4.31'), ('Африка', '4.24'),\
 # ('Поясни', '3.39'), ('Кавачай', '4.39'), ('Той день', '3.58'),\
 # ('Відпусти', '3.52'), ('Мало мені', '5.06'), ('Фіалки мої', '3.43'),\
 # ('Я на небі був', '3.19'), ('Коли тебе нема', '3.17')]
 #
 #    >>> sort_songs(song_titles, length_songs, last_word)
 #    [('Африка', '4.24'), ('Відпусти', '3.52'), ('Етюд', '2.21'),\
 # ('Кавачай', '4.39'), ('Поясни', '3.39'), ('Сосни', '4.31'),\
 # ('Я на небі був', '3.19'), ('Той день', '3.58'), ('Мало мені', '5.06'),\
 # ('Фіалки мої', '3.43'), ('Коли тебе нема', '3.17')]
    """
    if len(song_titles) != len(length_songs):
        return None
    for i in length_songs:
        for j in song_titles:
            if isinstance(i, str) is False or isinstance(j, str) is False:
                return None
            else:
                x = zip(song_titles, length_songs)
                return(sorted(x, key=key))

# def song_length(x):
#     """(zip) -> int
#
#     Return the time of the song
#     """
#     time = x[1].split(".")
#     return (int(time[0]) * 60 + int(time[1]))
#
# def title_length(x):
#     """(zip) -> int
#
#     Return lenght of the name of the song_length
#     """
#     return len(x[0])
#
# def last_word(x):
#     """(zip) -> str
#
#     Return last word of the name of the song to compare
#     """
#     words = x[0].split(" ")
#     return words[-1]
#
# def sort_songs(song_titles, length_songs, key):
#     """(list, list, function) -> list
#
#     Return list of sorted values due to the key
#
#     >>> sort_songs(song_titles, length_songs, song_length)
#     [('Етюд', '2.21'), ('Коли тебе нема', '3.17'), ('Я на небі був', '3.19'),
#     ('Поясни', '3.39'), ('Фіалки мої', '3.43'), ('Відпусти', '3.52'),
#     ('Той день', '3.58'), ('Африка', '4.24'), ('Сосни', '4.31'),
#     ('Кавачай', '4.39'), ('Мало мені', '5.06')]
#
#     >>> sort_songs(song_titles, length_songs, title_length)
#     [('Етюд', '2.21'), ('Сосни', '4.31'), ('Африка', '4.24'),
#     ('Поясни', '3.39'), ('Кавачай', '4.39'), ('Той день', '3.58'),
#     ('Відпусти', '3.52'), ('Мало мені', '5.06'), ('Фіалки мої', '3.43'),
#     ('Я на небі був', '3.19'), ('Коли тебе нема', '3.17')]
#
#     >>> sort_songs(song_titles, length_songs, last_word)
#     [('Африка', '4.24'), ('Відпусти', '3.52'), ('Етюд', '2.21'),
#     ('Кавачай', '4.39'), ('Поясни', '3.39'), ('Сосни', '4.31'),
#     ('Я на небі був', '3.19'), ('Той день', '3.58'), ('Мало мені', '5.06'),
#     ('Фіалки мої', '3.43'), ('Коли тебе нема', '3.17')]
#     """
#     if len(song_titles) != len(length_songs):
#         return None
#     if filter(lambda i: isinstance(i, str) is False, song_titles)\
#     or filter(lambda i: isinstance(i, str) is False, length_songs):
#         return "dfgl"
#     x = zip(song_titles, length_songs)
#     return(sorted(x, key=key))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
