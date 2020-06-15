from chunk import make_all_sentences_chunks_list
import pydot_ng as pydot

F_NAME = "neko.txt.cabocha"


"""
びにおもちろいわと	名詞,一般,*,*,*,*,*
云う	動詞,自立,*,*,五段・ワ行促音便,基本形,云う,イウ,イウ
のようなものもちゃんと管理する
"""
def _45():
    
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
                            case_pattern.append(src_morph.surface)
                
                if case_pattern:
                    verb_case_patterns.append(verb_base+"\t"+" ".join(sorted(case_pattern)))
    
    for verb_case_pattern in verb_case_patterns:
        print(verb_case_pattern)

if __name__ == "__main__":
    _45()


"""
sort 45 | uniq -c | sort -r | head -10
565 云う    と
442 する    を
249 思う    と
199 ある    が
189 なる    に
174 する    に
173 見る    て
127 する    と
117 する    が
105 する    に を
"""

"""
grep -E "^する" 45 | sort | uniq -c | sort -r | head -10
442 する  を
174 する に
127 する と
117 する が
105 する に を
86 する て を
59 する は
58 する て
57 する が を
48 する から
"""

"""
grep -E "^見る" 45 | sort | uniq -c | sort -r | head -10
173 見る  て
94 見る を
21 見る て て
20 見る から
18 見る て を
14 見る と
12 見る から て
12 見る で
11 見る て は
8 見る に
"""

"""
grep -E "^与える" 45 | sort | uniq -c | sort -r | head -10
3 与える  に を
2 与える  て に は を
1 与える  ば を
1 与える  に に対して のみ は は も
1 与える  て も を
1 与える  て に を
1 与える  て に に は を
1 与える  だけ で に を
1 与える  たり て に を
1 与える  けれども に は を
"""