from chunk import make_all_sentences_chunks_list
import pydot_ng as pydot

F_NAME = "neko.txt.cabocha"


def _48():
    
    contents = make_all_sentences_chunks_list(F_NAME)

    dag_from_norm = []

    for sentence in contents:

        
        for chunk in sentence:
            
            node_list = []
            norm = None
            
            for chunk_morph in chunk.morphs:
                if chunk_morph.pos == "名詞": 
                    norm = "".join(make_morphs_list_dispite_symbol(chunk.morphs))
                    node_list.append(norm)
                    break

            if norm:

                next_node = chunk.dst
                
                while next_node != -1:

                    norm = "".join(make_morphs_list_dispite_symbol(sentence[next_node].morphs))
                    node_list.append(norm)
                    next_node = sentence[next_node].dst
                
                dag_from_norm.append(node_list)
    
    for dag_node_list in dag_from_norm:
        print(" -> ".join(dag_node_list))


def make_morphs_list_dispite_symbol(morphs):
    res = []
    for morph in morphs:
        if morph.pos == "記号": continue
        res.append(morph.surface)
    return res

if __name__ == "__main__":
    _48()

"""
一
吾輩は -> 猫である
猫である
名前は -> 無い
どこで -> 生れたか -> つかぬ
見当が -> つかぬ
何でも -> 薄暗い -> 所で -> 泣いて -> 記憶している
所で -> 泣いて -> 記憶している
ニャーニャー -> 泣いて -> 記憶している
いた事だけは -> 記憶している
記憶している
"""

"""
根だけのnodeも出力するのか．．．．一応出力しておく
"""