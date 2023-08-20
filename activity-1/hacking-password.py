import hashlib
import time
import os
start_time = time.time()
c = 0
target = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"


def possible_word(word, full_word, i, len_word, lst):
    if i == len_word:
        lst.append(word)
        return lst
    if full_word[i] == 'o':
        lst = possible_word(word + '0', full_word, i+1, len_word, lst)
    if full_word[i] == 'l':
        lst = possible_word(word + '1', full_word, i+1, len_word, lst)
    if full_word[i] == 'i':
        lst = possible_word(word + '1', full_word, i+1, len_word, lst)
    lst = possible_word(
        word + full_word[i].lower(), full_word, i+1, len_word, lst)
    lst = possible_word(
        word + full_word[i].upper(), full_word, i+1, len_word, lst)
    return lst


def get_answer(word):
    word = word.lower()
    pos_lst = possible_word("", word, 0, len(word), [])
    for comb_word in pos_lst:
        if hashlib.sha1(comb_word.encode()).hexdigest() == target:
            return comb_word
        elif hashlib.md5(comb_word.encode()).hexdigest() == target:
            return comb_word
    return ""


with open("10k-most-common.txt", "r") as f:
    words = f.read().splitlines()
    ans = ""
    got_ans = False
    for word in words:
        ans = get_answer(word)
        if ans != "":
            got_ans = True
            break
    if got_ans:
        print(ans)
    else:
        print("This word is not in 10k most common password")

print("Finished in: " + str(time.time() - start_time) + " sec")
