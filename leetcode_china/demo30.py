from typing import List

def demo30(words, s):
    map1 = {}
    for word in words:
        if map1.get(word):
            map1[word] += 1
        else:
            map1[word] = 1

    n = len(word)
    word_n = len(word[0])
    for 