def _30():
    
    res = []

    with open("neko.txt.mecab", encoding="utf-8") as target:
        
        # 改行コードごとでsplit
        lines = target.read().split("\n")
        
        # 一文を格納するlist
        tmp = []

        for line in lines:

            # EOSか最終行なら一文をresに追加
            if line == "EOS" or line == "":
                if tmp: res.append(tmp)
                tmp = []
            else:
                word, feature_str = line.split("\t")
                features = feature_str.split(",")
                tmp.append(
                    {
                       "surface": word,
                       "base": features[6],
                       "pos": features[0],
                       "pos1": features[1]
                    }
                )
    return res

"""
[[{'surface': '一', 'base': '一', 'pos': '名詞', 'pos1': '数'}],
 [{'surface': '\u3000', 'base': '\u3000', 'pos': '記号', 'pos1': '空白'}, 
    {'surface': '吾輩', 'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞'},
    {'surface': 'は', 'base': 'は', 'pos': '助詞', 'pos1': '係助詞'}, 
    {'surface': '猫', 'base': '猫', 'pos': '名詞', 'pos1': '一般'}, 
    {'surface': 'で', 'base': 'だ', 'pos': '助動詞', 'pos1': '*'}, 
    {'surface': 'ある', 'base': 'ある', 'pos': '助動詞',.... 
"""



if __name__ == "__main__":
    print(_30())