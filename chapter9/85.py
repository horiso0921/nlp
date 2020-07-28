from scipy import sparse, io
import numpy as np
# decomposition.TruncatedSVDが疎行列に対応しているらしい
from sklearn.decomposition import TruncatedSVD
def _85():

    matrix = io.loadmat("matrix")["matrix"]
    m = TruncatedSVD(300)
    matrix = m.fit_transform(matrix)
    print(matrix.shape)
    np.save("matrix", matrix)


if __name__ == "__main__":
    _85()