from gensim.models import word2vec
import csv
lis_fname = ["94.csv","94_85.csv"]

def spearman(fname):

    with open(fname) as target:

        reader = csv.reader(target)
        l = [row for row in reader]
        scores = [[float(row[2]), float(row[3])] for row in l]

        scores.sort()
        for i in range(len(scores)):
            scores[i][0] = i

        scores.sort(key=lambda x:x[1])
        for i in range(len(scores)):
            scores[i][1] = i

        N = len(scores)
        D = sum((human - predict) ** 2 for human, predict in scores)
        res = 1 - (6 * D) / (N ** 3 - N)

        return res

def _95():    
    for fname in lis_fname:
        print(fname,spearman(fname))

if __name__ == "__main__":
    _95()

"""
94.csv 0.7012340842525219
94_85.csv 0.5009328936081301
"""