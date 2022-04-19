import random
from files.functions import *

f = open("files/words.txt",'r')
wordlist=f.readlines()
for i in range(len(wordlist)):
    wordlist[i]=wordlist[i].strip()

shuffle(wordlist)
guesses = [guess("toeas","11121"),guess("kaama","21311"),guess("flaky","13321"),guess("clank","23313"),guess("plack","13333")]
correct_letter_list =""
for i in guesses:
    wordlist=remove_words(i,wordlist)
    for j in i.list:
        if j[1]!="1" and j[0] not in correct_letter_list:
            correct_letter_list+=j[0]
print(correct_letter_list)
shuffle(wordlist)
best_word = score_list(wordlist,correct_letter_list)
print(best_word+" "+ str(score_word(best_word,wordlist,correct_letter_list)))