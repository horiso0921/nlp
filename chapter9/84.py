import random
import math
import pickle
from collections import defaultdict
from scipy import sparse, io
fname_tc_func = "tc_func"
fname_t_func = "t_func"
fname_c_func = "c_func"
fname_t_index = "t_index"
def _84():

    with open(fname_t_func, "rb") as f_data:
        t_func = pickle.load(f_data)
    
    with open(fname_c_func, "rb") as f_data:
        c_func = pickle.load(f_data)

    t_index = defaultdict(int)
    c_index = defaultdict(int)

    for t_i, t in enumerate(t_func.keys()):
        t_index[t] = t_i
    for c_i, c in enumerate(c_func.keys()):
        c_index[c] = c_i

    with open(fname_tc_func, "rb") as f_data:
        tc_func = pickle.load(f_data)
    
    matrix = sparse.lil_matrix((t_i+1, c_i+1))
    N = len(tc_func.keys())
    clc_ppmi = lambda t,c,f_tc: max(math.log((N * f_tc) / (t_func[t] * c_func[c])), 0)

    for key, f_tc in tc_func.items():
        if f_tc >= 10:
            t, c = key.split("\t")
            matrix[t_index[t], c_index[c]] = clc_ppmi(t, c, f_tc)

    io.savemat("matrix", {"matrix": matrix})

    with open(fname_t_index, "wb") as target:
        pickle.dump(t_index, target)

if __name__ == "__main__":
    _84()
