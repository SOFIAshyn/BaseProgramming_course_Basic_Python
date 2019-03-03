def nearestWords(wordList, word):
    new = []
    for lst_word in wordList:
        count = 0
        if len(word) == len(lst_word):
            for letter in range(len(word)):
                if word[letter] == lst_word[letter]:
                    new.append(lst_word)
    new = list(set(new))
    return new

print(nearestWords(['cats','snarf','carts','cat','bats','cbts','abcd'],'cats'))
