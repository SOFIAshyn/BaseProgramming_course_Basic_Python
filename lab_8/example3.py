from utils import process_file
import random

text = process_file("data.txt")
words = text.split()


dct = {}
for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i+1]
    if word not in dct:
        dct[word] = set()
    dct[word].add(next_word)
print(dct)


new_text = [random.choice(list(dct.keys()))]
for i in range(100):
    # last_word = new_text[-1]
    # possible_words = list(dct[last_word])
    # new_text.append(random.choice(possible_words))

    new_text.append(random.choice(list(dct[new_text[-1]])))
print(new_text)
