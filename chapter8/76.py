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

def _76():
    stemmer = stem.PorterStemmer()
    W = defaultdict(float)
    with open("73", "r", encoding="latin_1") as target:
        for line in target:
            word, label = line.rstrip().split()
            W[word] = float(label) 

    with open("sentiment.txt", "r", encoding="latin_1") as target:
        for line in target:
            AnsLavel, line = line[:2], line[3:]  
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
                lavel = "+1"
            else:
                lavel = "-1"
            
            print(f"{AnsLavel}\t{lavel}\t{predict}")


if __name__ == "__main__":
    _76()

"""
-1	-1	-0.4273930313090759
-1	-1	-0.7893002744162573
+1	+1	0.08847097165861628
+1	+1	0.7386678630527377
+1	+1	0.4748116551538386
-1	-1	-0.8636548976467455
+1	+1	0.33922185838287655
-1	-1	-0.7246554106766525
-1	-1	-0.012220748807445725
+1	-1	-0.3904822493624749
+1	+1	0.006177481425583942
+1	-1	-0.2161412661594344
-1	-1	-0.19624569181769302
....
"""