import pickle
from collections import defaultdict
from scipy import io
import numpy as np
fname_t_func = "t_index"
out_fname = "89_out"
def _89():
    with open(fname_t_func, "rb") as f_data:
        t_index = pickle.load(f_data)

    matrix = io.loadmat("85")["matrix"]
    Spain_matrix = matrix[t_index["Spain"]]
    Madrid_matrix = matrix[t_index["Madrid"]]
    Athens_matrix = matrix[t_index["Athens"]]

    target_matrix = Spain_matrix - Madrid_matrix + Athens_matrix

    cossim_dict = defaultdict(int)

    for t_i in t_index.keys():
        t_i_matrix = matrix[t_index[t_i]]
        nolm = np.linalg.norm(target_matrix) * np.linalg.norm(t_i_matrix)
        if nolm:
            cossim_dict[t_i] = np.dot(target_matrix, t_i_matrix) / nolm
    
    sorted_cossim_dict = sorted(cossim_dict.items(), key=lambda x: -x[1])

    with open(out_fname,"w") as out_target:
        for key, value in sorted_cossim_dict[:11]:
            print(key, value, file=out_target)
if __name__ == "__main__":
    _89()

"""
Sweden 0.8723148629358709
Austria 0.8596003567888679
Belgium 0.8458647025306972
Netherlands 0.844956129749838
Turkey 0.841417121472239
Spain 0.8413030563107298
Vichy 0.8335288959316792
Télévisions 0.8335288959316792
Greece 0.8313518302306707
Copenhagen 0.82709625675208
Denmark 0.823649844372748
"""