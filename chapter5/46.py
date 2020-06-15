from chunk import make_all_sentences_chunks_list
import pydot_ng as pydot

F_NAME = "neko.txt.cabocha"


"""
びにおもちろいわと	名詞,一般,*,*,*,*,*
云う	動詞,自立,*,*,五段・ワ行促音便,基本形,云う,イウ,イウ
のようなものもちゃんと管理する
"""
def _46():
    
    contents = make_all_sentences_chunks_list(F_NAME)

    verb_case_patterns = []

    for sentence in contents:

        
        for chunk in sentence:
            
            case_pattern = []
            verb_base = None
            
            for chunk_morph in chunk.morphs:
                if chunk_morph.pos == "動詞": 
                    verb_base = chunk_morph.base
                    break
                
            if verb_base:

                for i in chunk.srcs:
                    
                    for src_morph in sentence[i].morphs:
                        if src_morph.pos == "助詞":
                            morphs = make_morphs_list_dispite_symbol(sentence[i].morphs)
                            case_pattern.append((src_morph.surface, "".join(morphs)))

                
                if case_pattern:
                    case_pattern.sort()
                    pps, phrase = zip(*case_pattern)
                    verb_case_patterns.append(verb_base+"\t"+" ".join(pps)+"\t"+" ".join(phrase))
    
    for verb_case_pattern in verb_case_patterns:
        print(verb_case_pattern)


def make_morphs_list_dispite_symbol(morphs):
    res = []
    for morph in morphs:
        if morph.pos == "記号": continue
        res.append(morph.surface)
    return res

if __name__ == "__main__":
    _46()

"""
生れる	で	　どこで
つく	か が	生れたか 見当が
泣く	で	所で
する	だけ て は	いた事だけは 泣いて いた事だけは
始める	で	ここで
見る	は を	吾輩は ものを
聞く	で	あとで
捕える	を	我々を
煮る	て	捕えて
食う	て	煮て
....
"""