from chunk import make_all_sentences_chunks_list

F_NAME = "neko.txt.cabocha"

def _43():
    
    contents = make_all_sentences_chunks_list(F_NAME)

    for sentence in contents:
        for chunk in sentence:
            if chunk.dst != -1:
                chunk_morphs = chunk.morphs
                dst_morphs = sentence[chunk.dst].morphs
                
                if have_noun_morphs(chunk_morphs) and have_verb_morphs(dst_morphs):
                    chunk_text_list = make_morphs_list_dispite_symbol(chunk_morphs)
                    dst_text_list = make_morphs_list_dispite_symbol(dst_morphs)

                    print("".join(chunk_text_list)+"\t"+"".join(dst_text_list))

def have_noun_morphs(morphs):
    for morph in morphs:
        if morph.pos == "名詞": return True
    return False

def have_verb_morphs(morphs):
    for morph in morphs:
        if morph.pos == "動詞": return True
    return False

def make_morphs_list_dispite_symbol(morphs):
    res = []
    for morph in morphs:
        if morph.pos == "記号": continue
        res.append(morph.surface)
    return res

if __name__ == "__main__":
    _43()

"""
どこで	生れたか
見当が	つかぬ
所で	泣いて
ニャーニャー	泣いて
いた事だけは	記憶している
吾輩は	見た
ここで	始めて
ものを	見た
あとで	聞くと
....（後略）
"""