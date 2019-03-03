#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random


def generate_text(N, articles, nouns, verbs, adjectives):
    """
    (int, list, list, list, list) -> str

    Return string with poem.

    >>> random.seed(4)
    >>> generate_text(5, ["the", "а", "his", "her", "my"], ["cat", "dog", "man", "woman"], ["sang", "ran", "jumped"], ["loudly", "quietly", "well", "badly"])
    'а man sang\\nа cat sang\\nmy man sang\\nhis dog sang well\\nthe man ran quietly\\n'
    """
    a = ""
    for i in range(N):
        ar = random.choice(articles)
        n = random.choice(nouns)
        v = random.choice(verbs)
        ad = random.choice(adjectives)
        variant = random.randint(1, 2)
        if variant == 1:
            str = ar + " " + n + " " + v + " " + ad
        else:
            str = ar + " " + n + " " + v
        a += str + "\n"
    return a


try:
    N = int(sys.argv[1])
except IndexError:
    N = 5

if  0 < N < 11:
    articles = ["the", "а", "his", "her", "my"]
    nouns = ["cat", "dog", "man", "woman"]
    verbs = ["sang", "ran", "jumped"]
    adjectives = ["loudly", "quietly", "well", "badly"]
    print(generate_text(N, articles, nouns, verbs, adjectives), end = "")
else:
    print("Your number should be in range 1 to 10.")

import doctest
print(doctest.testmod())
