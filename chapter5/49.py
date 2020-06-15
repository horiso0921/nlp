from chunk import make_all_sentences_chunks_list
from collections import defaultdict
import pydot_ng as pydot

F_NAME = "neko.txt.cabocha"


def _49():
    
    contents = make_all_sentences_chunks_list(F_NAME)

    dag_from_norm = []

    for sentence in contents:

        norm_phrase_of_sentence = defaultdict(int)

        for i, chunk in enumerate(sentence):
            
            for chunk_morph in chunk.morphs:
                if chunk_morph.pos == "名詞": 
                    norm_phrase_of_sentence[i] = 1
                    break
        
        check = defaultdict(int)
        from_chunk_to_root_list = defaultdict(list)
        
        for i, chunk in enumerate(sentence):

            if not norm_phrase_of_sentence[i]: continue
            
            node_index_list = [i]
            node_list = []
            norm = None
        
            norm = "".join(replace_left_norm_to_X(chunk.morphs, "X"))
            node_list.append(norm)

            next_node = chunk.dst                        

            while next_node != -1:
                if norm_phrase_of_sentence[next_node]:
                    check[(i, next_node)] = 1
                    norm = "Y"
                    print(" -> ".join(node_list + [norm]))
                norm = "".join(make_morphs_list_dispite_symbol(sentence[next_node].morphs))
                node_list.append(norm)
                node_index_list.append(next_node)
                next_node = sentence[next_node].dst

            from_chunk_to_root_list[i] = node_index_list

        for i, chunk in enumerate(sentence):
            if not norm_phrase_of_sentence[i]: continue
            for j in range(i+1,len(sentence)):
                if not norm_phrase_of_sentence[j]: continue
                if check[(i,j)]: continue
                res = []
                for k in from_chunk_to_root_list[j]:
                    if k in from_chunk_to_root_list[i]:
                        break
                
                norm = "".join(replace_left_norm_to_X(chunk.morphs, "X"))
                node_list = []
                node_list.append(norm)

                next_node = chunk.dst 

                while next_node != k:
                    norm = "".join(make_morphs_list_dispite_symbol(sentence[next_node].morphs))
                    node_list.append(norm)
                    next_node = sentence[next_node].dst

                res.append(" -> ".join(node_list))

                norm = "".join(replace_left_norm_to_X(sentence[j].morphs, "Y"))
                node_list = []
                node_list.append(norm)

                next_node = sentence[j].dst
                
                while next_node != k:
                    norm = "".join(make_morphs_list_dispite_symbol(sentence[next_node].morphs))
                    node_list.append(norm)
                    next_node = sentence[next_node].dst
                
                res.append(" -> ".join(node_list))

                res.append("".join(make_morphs_list_dispite_symbol(sentence[k].morphs)))

                print(" | ".join(res))


def make_morphs_list_dispite_symbol(morphs) -> list:
    res = []
    for morph in morphs:
        if morph.pos == "記号": continue
        res.append(morph.surface)
    return res

def replace_left_norm_to_X(morphs, X) -> list:
    res = []
    f = 1
    for morph in morphs:
        if morph.pos == "記号": continue
        if morph.pos == "名詞" and f:
            res.append(X)
            f = 0
        else:
            res.append(morph.surface)
    return res

if __name__ == "__main__":
    _49()

"""
Xは -> Y
Xで -> 生れたか | Yが | つかぬ
Xでも -> 薄暗い -> Y
Xでも -> 薄暗い -> 所で -> 泣いて -> Y
Xで -> 泣いて -> Y
X -> 泣いて -> Y
Xだけは -> Y
Xでも -> 薄暗い -> 所で | Y | 泣いて
Xでも -> 薄暗い -> 所で -> 泣いて | Yだけは | 記憶している
Xで | Y | 泣いて
Xで -> 泣いて | Yだけは | 記憶している
X -> 泣いて | Yだけは | 記憶している
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 聞くと -> Y
Xは -> Y
Xという -> Y
....
"""