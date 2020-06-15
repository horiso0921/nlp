from chunk import make_all_sentences_chunks_list

F_NAME = "neko.txt.cabocha"

def _42():
    
    contents = make_all_sentences_chunks_list(F_NAME)

    for sentence in contents:
        for chunk in sentence:
            if chunk.dst != -1:
                chunk_morphs = chunk.morphs
                dst_morphs = sentence[chunk.dst].morphs
                
                chunk_text_list = make_morphs_list_dispite_symbol(chunk_morphs)
                dst_text_list = make_morphs_list_dispite_symbol(dst_morphs)

                print("".join(chunk_text_list)+"\t"+"".join(dst_text_list))

def make_morphs_list_dispite_symbol(morphs):
    res = []
    for morph in morphs:
        if morph.pos == "記号": continue
        res.append(morph.surface)
    return res

if __name__ == "__main__":
    _42()

"""
	猫である
吾輩は	猫である
名前は	無い
まだ	無い
どこで	生れたか
生れたか	つかぬ
とんと	つかぬ
見当が	つかぬ
何でも	薄暗い
薄暗い	所で
じめじめした	所で
所で	泣いて
ニャーニャー	泣いて
泣いて	記憶している
いた事だけは	記憶している
.....(後略)
"""