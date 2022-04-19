import random
import math
contains_check = 3 #test 3 vs 2, 1 is random guess


def check_word(word1,word2,letters):
    number = ""
    for i in range(5):
        if word1[i] in letters:
            number+="3"
        else: 
            number+="1"
    g=guess(word1,number)
    return g.chalange(word2) 

def score_word(word,list,letters):
    score = 0 
    for i in list:
        if not check_word(word,i,letters):
            score+=1
    return score

def score_list(list,letters):
    best_word="sneed"
    best_score=0
    for i in list:
        num = score_word(i,list,letters)
        if num >best_score:
            best_score=num
            best_word=i
        if list.index(i)%100==0:
            print(math.floor(list.index(i)/len(list)*10000)/100)
    return best_word


def shuffle(list):
    for i in range(10):
        random.shuffle(list)
        list.reverse()
def find_all(word,char):
    start=0
    results = []
    while True:
        start = word.find(char,start)
        if start == -1:return results
        results.append(start)
        start+=len(char)

class guess:
    def __init__(self,word,color):
        self.word = word
        self.list = []
        for i in range(5):
            self.list.append((word[i],color[i],i))
    def chalange(self,word):
        counter = []
        letters =""
        for i in self.word:
            if self.word.count(i) >1:
                total = 0
                for j in find_all(self.word,i):
                    if int(self.list[j][1]) >1:
                        total +=1
                if total >=1:
                    counter.append((i,total))
                    letters+=i      

        for i in self.list:
            if i[1]=='1' and i[0] in word and i[0] not in letters:
                return False
            if i[1]=='2' and i[0] not in letters and (word[i[2]]==i[0] or i[0] not in word):
                return False
            if i[1]=='3' and not word[i[2]]==i[0]:
                return False
            for j in counter:
                if j[1]==1 and word.count(j[0])>1:
                    return False
                if word.count(j[0])< j[1]:
                    return False

        return True

def remove_words(guess,list):
    j = range(len(list)-1,-1,-1)
    for i in j:
        if not guess.chalange(list[i]):
            list.pop(i)
        elif list[i]==guess.word:
            list.pop(i)
    return list
    