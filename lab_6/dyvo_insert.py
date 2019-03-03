def dyvo_insert(sentence, flag):
    """(str, str) -> str
    Inserting word "диво" before every word that starts with flag.

    >>> dyvo_insert('Кит кота по хвилях катав - кит у воді, кіт на киті.', 'ки')
    диво Кит кота по хвилях катав - диво кит у воді, кіт на диво киті.
    """
    new_sentence = ''
    for each in sentence.split():
        if each[:2].lower() == 'ки':
            new_sentence += 'диво '
        if each == (sentence.split())[-1]:
            new_sentence += each
        else:
            new_sentence += each + ' '
    return new_sentence

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
