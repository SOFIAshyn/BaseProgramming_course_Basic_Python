def film_analysis():
    """
    Function run all proceses and find number of films
    that use two keywords with maximal frequency.
    This program use data from imdb database file keywords.list.
    """

    print("""This program find number of films
that use two keywords with maximal frequency.
This program use data from imdb database file keywords.list.""")
    keywords, film_keywords = input_from_file()
    keyw1, keyw2 = freq_keywords(keywords)
    number_films = find_films(film_keywords, keyw1, keyw2)
    print("""\nFilms analysis result
Keywords {0} and {1} are using
in {2} films""".format(keyw1, keyw2, number_films))


def get_generator(file):
    while file:
        yield file.readline()


def input_from_file():
    """
    Returns the list of tuple and generator of dictionary
    """
    f = open(input("Please type the file name and path to file if need: "),\
             encoding='utf-8', errors='ignore')
    gen_get = get_generator(f)
    data = next(gen_get)
    while not data.startswith("   keywords in use:"):
        data = next(gen_get)
    lst = []
    while not data.startswith("5: Sub"):
        data = next(gen_get).strip()
        lst.append(data)

    keywords = list(map(lambda x: x.split("\t"), lst))
    keywords = list(filter(lambda x: x != '', \
    (x for x in [lst for lst in keywords])))
    keywords = [(int(w.split()[1][1:-1]), w.split()[0])
                for lst1 in keywords[:-1] for w in filter(lambda w: w, lst1)]

    while not data.startswith("8: THE"):
        data = next(gen_get)

    film_keywords = {}
    for line in f:
        film, keyword = line.strip().split("\t")[0], \
                        line.strip().split("\t")[-1]
        if keyword not in film_keywords:
            film_keywords[keyword] = [film]
        else:
            film_keywords[keyword].append(film)
    f.close()

    return keywords, film_keywords


def freq_keywords(keywords):
    """
    (list of tuple) -> tuple of (srt, str)

    Find the indexes of two maximum items in the tuple list and
    return two keywordsof those indexes

    output: ('independent-film', 'character-name-in-title')
    """
    keyw1_keyw2 = (lambda num_el: keywords[num_el[0]], \
                   sorted(keywords)[-2:])[1]
    keyw1, keyw2 = (part[1] for part in keyw1_keyw2)

    return keyw1, keyw2


def find_films(film_keywords, keyw1, keyw2):
    """
    Return number of films that use keywords
    """
    return len(set(film_keywords[keyw1] + film_keywords[keyw2]))


if __name__ == '__main__':
    film_analysis()
