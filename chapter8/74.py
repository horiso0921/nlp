import math
from nltk import stem
from nltk.corpus import stopwords
from collections import defaultdict
STOP_WORDS = stopwords.words('english')

def checkstopwords(word):
    """
    >>> checkstopwords("i")
    True
    >>> checkstopwords("me")
    True
    >>> checkstopwords("won")
    True
    >>> checkstopwords("point")
    False
    >>> checkstopwords("cabocha")
    False
    """
    return word.lower() in STOP_WORDS


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

def _74():
    stemmer = stem.PorterStemmer()
    W = defaultdict(float)
    with open("73", "r", encoding="latin_1") as target:
        for line in target:
            word, label = line.rstrip().split()
            W[word] = float(label) 
    while 1:
        print("If you want to end, you should input only 'N'")
        line = input("Please input a sentence > ")

        if line == "N": break
        
        line_features = []
        for word in line.split():
            if word in ["," , "." , ":" , ";", "--", "-"]: continue
            if not checkstopwords(word):
                feature = stemmer.stem(word)
                line_features.append(feature)
        a = sum(W[x] for x in line_features)
        predict = sigmoid(a)
        predict = (predict * 2) - 1

        if predict > 0:
            print("label +1",end=" ")
        elif predict < 0:
            print("label -1",end=" ")
        else:
            print("label 0",end=" ")
        print("predict ",predict)
        print("===========")

if __name__ == "__main__":
    _74()

"""
If you want to end, you should input only 'N'
Please input a sentence > by the time it ends in a rush of sequins , flashbulbs , blaring brass and back-stabbing babes , it has said plenty about how show business has infiltrated every corner of society -- and not always for the better .
label -1 predict  -0.13302884495852552
===========
If you want to end, you should input only 'N'
Please input a sentence >  before long , the film starts playing like general hospital crossed with a saturday night live spoof of dog day afternoon .
label -1 predict  -0.5729294794526296
===========
If you want to end, you should input only 'N'
Please input a sentence > N
"""