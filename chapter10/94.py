from gensim.models import word2vec
import csv
fname = "wordsim353/combined.csv"

def _94():    
    model = word2vec.Word2Vec.load("model")
    with open(fname) as target, open("94.csv","w") as out:
        reader = csv.reader(target)
        l = [row for row in reader]
        for line in l[1:]:
            word1, word2, score = line
            cossim = model.wv.similarity(word1, word2)
            print(f"{word1},{word2},{score},{cossim}", file=out)

def run_based_85():
    import pickle
    from collections import defaultdict
    import numpy as np
    fname_t_func = "../chapter9/t_index"
    with open(fname_t_func, "rb") as f_data:
        t_index = pickle.load(f_data)

    matrix = np.load("../chapter9/matrix.npy")
    with open(fname, "r") as target, open("94_85.csv","w") as out:
        reader = csv.reader(target)
        l = [row for row in reader]
        for line in l[1:]:
            word1, word2, score = line
            if word1 in t_index and word2 in t_index:
                vec1 = matrix[t_index[word1]]
                vec2 = matrix[t_index[word2]]
                nolm = np.linalg.norm(vec1) * np.linalg.norm(vec2)
                if nolm:
                    cossim = np.dot(vec1, vec2) / nolm
                    print(f"{word1},{word2},{score},{cossim}", file=out)

if __name__ == "__main__":
    _94()
    run_based_85()

"""
_94
love,sex,6.77,0.2682211399078369
tiger,cat,7.35,0.5939254760742188
tiger,tiger,10.00,0.9999999403953552
book,paper,7.46,0.4062546491622925
computer,keyboard,7.62,0.4314471185207367
computer,internet,7.58,0.40162670612335205
plane,car,5.77,0.34319961071014404
train,car,6.31,0.42242518067359924
telephone,communication,7.50,0.36818501353263855
television,radio,6.77,0.5589839220046997
"""

"""
_94_85
love,sex,6.77,0.2525520668969308
tiger,cat,7.35,0.15423760268120565
tiger,tiger,10.00,0.9999999999999999
book,paper,7.46,0.48804847181147015
computer,keyboard,7.62,0.23156649505505378
computer,internet,7.58,0.5007865837619766
plane,car,5.77,0.23633799248351323
train,car,6.31,0.41164581065803574
telephone,communication,7.50,0.8215968071055874
television,radio,6.77,0.752135657427578
"""