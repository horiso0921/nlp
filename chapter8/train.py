from collections import defaultdict
import math
"""
確率的勾配法を用いる
参考
http://www.chokkan.org/publication/survey/prml_chapter4_discriminative_slides.pdf
"""

eta0 = 0.1 #学習率
etan = 0.9999 #学習率減少率
N = 10662 #ファイルの行数

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

def update(W, features, label, eta):
    a = sum([W[x] for x in features])  
    predict = sigmoid(a)
    label = (label + 1) / 2

    for x in features:
        dif = eta * (predict - label)
        W[x] = W[x] - dif

def train(target):

    W = defaultdict(float)
    t = 1
    for line in target:
        words = line.split()
        label, features = words[0], words[1:]
        update(W, features, int(label),  eta0 / (1 + t / float(N)))
        t += 1
    
    return W
