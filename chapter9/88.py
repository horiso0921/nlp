import pickle
from collections import defaultdict
import numpy as np
fname_t_func = "t_index"
out_fname = "88_out"
def _88():
    
    with open(fname_t_func, "rb") as f_data:
        t_index = pickle.load(f_data)
    
    matrix = np.load("matrix.npy")
    England_matrix = matrix[t_index["England"]]

    cossim_dict = defaultdict(int)

    for t_i in t_index.keys():
        t_i_matrix = matrix[t_index[t_i]]
        nolm = np.linalg.norm(England_matrix) * np.linalg.norm(t_i_matrix)
        if nolm:
            cossim_dict[t_i] = np.dot(England_matrix, t_i_matrix) / nolm
    
    sorted_cossim_dict = sorted(cossim_dict.items(), key=lambda x: -x[1])

    with open(out_fname,"w") as out_target:
        for key, value in sorted_cossim_dict[:11]:
            print(key, value, file=out_target)
if __name__ == "__main__":
    _88()

"""
1/100スケール
England 1.0000000000000002
Cheshire 0.7186964637867348
Scotland 0.6220641699841934
Italy 0.6070207904793331
Wales 0.5728527624038094
Spain 0.5531774144839648
returned 0.5494862468272309
France 0.5409465632373546
Naples 0.5392799387902304
Germany 0.5378277592080488
Patriots 0.5310895238324331
"""

"""
1/10スケール
England 1.0
Normans 0.8353494143189643
selectors 0.8353494143189643
Herefordshire 0.8353494143189638
Quays 0.7595157973335063
RVC 0.7550887745062101
Nantwich 0.7550887745062097
Cumbria 0.7547995904349124
Wolds 0.7540935998929836
wicket-keeper 0.7461750695138935
Northamptonshire 0.7410175145629424
"""