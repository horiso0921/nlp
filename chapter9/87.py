import pickle
from collections import defaultdict
import numpy as np
fname_t_func = "t_index"
out_fname = "87_out"
def _87():
    with open(fname_t_func, "rb") as f_data:
        t_index = pickle.load(f_data)

    matrix = np.load("matrix.npy")
    United_States_matrix = matrix[t_index["United_States"]]
    US_matrix = matrix[t_index["U.S"]]
    nolm = np.linalg.norm(United_States_matrix) * np.linalg.norm(US_matrix)
    with open(out_fname,"w") as out_target:
        print(np.dot(United_States_matrix, US_matrix) / nolm, file=out_target)
if __name__ == "__main__":
    _87()

"""
0.8230089436712562
"""