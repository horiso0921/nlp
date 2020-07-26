import pickle
from collections import defaultdict
import numpy as np
from scipy import io
import word2vec
fname_input = '81_out'
fname_word2vec_out = 'word2vec.txt'
fname_t_index = 't_index'
fname_matrix = 'matrix'
def _90():

    word2vec.word2vec(train=fname_input, output=fname_word2vec_out,size=300)

    with open(fname_word2vec_out, 'rb') as target:

        size, dim = target.readline().split(' ')
        matrix = np.zeros([size, dim], dtype=np.float64)

        t_index = defaultdict(int)

        for i, line in enumerate(target):
            key, value = line.strip().split(' ')
            t_index[key] = i
            matrix[i] = map(float, value)

    io.savemat(fname_matrix, {'matrix': matrix})
    with open(fname_t_index, 'wb') as target:
        pickle.dump(t_index, target)



if __name__ == "__main__":
    _90()