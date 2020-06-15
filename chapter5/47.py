from chunk import make_all_sentences_chunks_list
import pydot_ng as pydot

F_NAME = "neko.txt.cabocha"


def _47():
    
    contents = make_all_sentences_chunks_list(F_NAME)

    verb_case_patterns = []

    for sentence in contents:

        
        for chunk in sentence:
            
            case_pattern = []
            sa_links = []
            verb_base = None
            
            for chunk_morph in chunk.morphs:
                if chunk_morph.pos == "動詞": 
                    verb_base = chunk_morph.base
                    break
                
            if verb_base:

                for i in chunk.srcs:
                    
                    src_morphs = sentence[i].morphs

                    for src_i in range(len(src_morphs) - 1):
                        if src_morphs[src_i].pos1 == "サ変接続" and src_morphs[src_i + 1].surface == "を":
                            sa_links.append(src_morphs[src_i].surface + src_morphs[src_i+1].surface + verb_base)
                        
                        elif src_morphs[src_i + 1].pos == "助詞":
                            morph = make_morphs_list_dispite_symbol(src_morphs)
                            case_pattern.append((src_morphs[src_i + 1].surface, "".join(morph)))


                if case_pattern:
                    case_pattern.sort()
                    pps, phrase = zip(*case_pattern)
                    for sa_link_verb in sa_links:
                        verb_case_patterns.append(sa_link_verb+"\t"+" ".join(pps)+"\t"+" ".join(phrase))
    
    for verb_case_pattern in verb_case_patterns:
        print(verb_case_pattern)


def make_morphs_list_dispite_symbol(morphs):
    res = []
    for morph in morphs:
        if morph.pos == "記号": continue
        res.append(morph.surface)
    return res

if __name__ == "__main__":
    _47()

"""
cut -f1 47 | sort | uniq -c | sort -r | head -10
26 返事をする
19 挨拶をする
12 話をする
8 質問をする
7 喧嘩をする
6 真似をする
5 質問をかける
5 相談をする
5 注意をする
5 昼寝をする
"""

"""
cut -f1,2 47 | sort | uniq -c | sort -r | head -10
4 返事をする      と
4 挨拶をする      から
3 返事をする      と は
3 挨拶をする      と
3 喧嘩をする      と
2 返事をする      から と
2 質問をかける    と は
2 議論をする      て
2 講義をする      で
2 覚悟をする      と
"""