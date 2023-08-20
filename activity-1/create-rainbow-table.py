import hashlib
import time
import os
start_time = time.time()
c = 0


def possible_word(word, full_word, i, len_word, lst):
    if i == len_word:
        lst.append(word)
        return lst
    if full_word[i] == 'o':
        lst = possible_word(word + '0', full_word, i+1, len_word, lst)
    elif full_word[i] == 'l' or full_word[i] == 'i':
        lst = possible_word(word + '1', full_word, i+1, len_word, lst)
    if full_word[i].islower():
        lst = possible_word(
            word + full_word[i].upper(), full_word, i+1, len_word, lst)
    lst = possible_word(
        word + full_word[i].lower(), full_word, i+1, len_word, lst)
    return lst


f = open("10k-most-common.txt", "r")
rp = open("rainbow-table.txt", "w")

words = f.read().splitlines()
for word in words:
    pos_lst = possible_word("", word, 0, len(word), [])
    for comb_word in pos_lst:
        h = hashlib.sha1(comb_word.encode()).hexdigest()
        text = comb_word + " " + h
        rp.write(text + "\n")

print("Finished in: " + str(time.time() - start_time) + " sec")
