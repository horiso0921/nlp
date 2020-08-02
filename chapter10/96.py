from gensim.models import word2vec
MODEL = word2vec.Word2Vec.load("model_m1_win15")
COUNTRY_PATH = "../chapter9/country.txt"

def _96():
    c = {}
    with open(COUNTRY_PATH) as target,  open("96", "w") as out:
        for line in target:
            word = line.strip().replace(' ', '_')
            if word in c: continue
            c[word] = 1
            try:
                matrix = MODEL.wv[word]
                print(word, end="\t", file=out)
                print(*matrix, file=out)
            except:
                pass
if __name__ == "__main__":
    _96()

"""
United_States	1.6922709 -1.1653358 -4.5630145 -0.35093668 (省略)
Isle_of_Man	0.44254324 0.497743 1.6241473 -0.56659985 1.843889 （省略）
"""