from gensim.models import word2vec
fname = "family_91"

def _91():    
    model = word2vec.Word2Vec.load("model")
    with open(fname, "r") as target, open("92","w") as out:
        for line in target:
            vec1, vec2, vec3, vec4 = line.rstrip().split()
            ans = model.wv.most_similar_cosmul(positive=[vec2, vec3], negative=[vec1],topn=1)
            print(f"{vec1} {vec2} {vec3} {vec4} {ans[0][0]} {ans[0][1]}", file=out)

def run_based_85():
    import pickle
    from collections import defaultdict
    import numpy as np
    fname_t_func = "../chapter9/t_index"
    with open(fname_t_func, "rb") as f_data:
        t_index = pickle.load(f_data)

    matrix = np.load("../chapter9/matrix.npy")
    with open(fname, "r") as target, open("92_85","w") as out:
        e = 0
        for line in target:
            vec1_str, vec2_str, vec3_str, vec4_str = line.rstrip().split()
            vec1 = matrix[t_index[vec1_str]]
            vec2 = matrix[t_index[vec2_str]]
            vec3 = matrix[t_index[vec3_str]]
            target_matrix = vec2 - vec1 + vec3

            cossim_max = ["", -1]

            for t_i in t_index.keys():
                t_i_matrix = matrix[t_index[t_i]]
                nolm = np.linalg.norm(target_matrix) * np.linalg.norm(t_i_matrix)
                if nolm:
                    cossim_tmp = np.dot(target_matrix, t_i_matrix) / nolm
                    if cossim_tmp > cossim_max[1]:
                        cossim_max = [t_i, cossim_tmp]
            print("end", e)
            e += 1
            print(f"{vec1_str} {vec2_str} {vec3_str} {vec4_str} {cossim_max[0]} {cossim_max[1]}", file=out)
            


if __name__ == "__main__":
    _91()
    run_based_85()
"""
head -10 92
boy girl brother sister sister 0.9287561774253845
boy girl brothers sisters sisters 0.9007980227470398
boy girl dad mom mom 0.9370443820953369
boy girl father mother mother 0.8997248411178589
boy girl grandfather grandmother grandmother 0.8639628291130066
boy girl grandpa grandma paudwal 0.8983207941055298
boy girl grandson granddaughter granddaughter 0.9143123030662537
boy girl groom bride bride 0.9589276909828186
boy girl he she she 0.9186397790908813
boy girl his her her 0.8954459428787231
brothers sisters husband wife sister-in-law 0.9124312400817871
"""

"""
head -10 92_85
boy girl brother sister brother 0.9902462737231142
boy girl brothers sisters brothers 0.9248816180409056
boy girl dad mom dad 0.9233130699354243
boy girl father mother father 0.9461352846806459
boy girl grandfather grandmother grandfather 0.963243925705584
boy girl grandpa grandma girl 0.7626886062165029
boy girl grandson granddaughter grandson 0.9897968404640591
boy girl groom bride girl 0.7758452920929134
boy girl he she girl 0.8248014528294453
boy girl his her his 0.9250676202430007
"""
