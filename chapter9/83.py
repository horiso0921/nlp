from collections import defaultdict
import pickle
fname = "82_out"
fname_tc_func = "tc_func"
fname_t_func = "t_func"
fname_c_func = "c_func"

def _83():
    tc_func = defaultdict(int)
    t_func = defaultdict(int)
    c_func = defaultdict(int)
    
    with open(fname, "r", encoding="utf-8") as target:
        for line in target:
            line = line.rstrip()
            tc_func[line] += 1
            t,c = line.split("\t")
            t_func[t] += 1
            c_func[c] += 1
    
    with open(fname_tc_func, "wb") as f_data:
        pickle.dump(tc_func, f_data)

    with open(fname_t_func, "wb") as f_data:
        pickle.dump(t_func, f_data)
    
    with open(fname_c_func, "wb") as f_data:
        pickle.dump(c_func, f_data)

if __name__ == "__main__":
    _83()
