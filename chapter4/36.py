from collections import defaultdict

def get_morpheme_dict_lists():
    """
    一文の一語づつの形態素が辞書で格納されて
    一文にlistで入っている
    上の一文の形態素の情報を一要素としたlistを返す
    """

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

def _36():

    morpheme_dict_lists = get_morpheme_dict_lists()

    words = defaultdict(int)
    for line in morpheme_dict_lists:
        for word in line:
            if word["pos"] != "記号":
                words[word["base"]] += 1
    

    # baseがうまく認識しないと*になってるよ...
    items = sorted(words.items(), key=lambda x: -x[1])
    words = list(map(lambda x: x[0], items))
    print(words[:30])

if __name__ == "__main__":
    _36()

"""
['の', 'て', 'は', 'に', 'を', 'だ', 'と', 'が', 'た', 
'する', 'ない', 'も', 'ある', '*', 'で', 'から', 'いる',
 'ん', 'か', '云う', '事', 'です', 'ます', 'なる', 'へ', 
 'う', 'もの', '君', '主人', 'ぬ']
"""