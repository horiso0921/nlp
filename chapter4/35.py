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

def _35():

    morpheme_dict_lists = get_morpheme_dict_lists()

    nouns = []
    tmp_nouns = []
    for line in morpheme_dict_lists:
        for word in line:
            if word["pos"] == "名詞":
                tmp_nouns.append(word["surface"])
            else:
                if tmp_nouns:
                    nouns.append("".join(tmp_nouns))
                    tmp_nouns = []
    # ここで気づいたけど many a slip 'twixt the cup and the lipが全部英語になってる（解決わからず） 
    print(nouns)

if __name__ == "__main__":
    _35()


"""
'一', '吾輩', '猫', '名前', 'どこ', '見当', '何', '所', 'ニャーニャー', 
'いた事', '記憶', '吾輩', 'ここ', '人間', 'もの', 'あと', 'それ', '書生', 
'人間中', '一番獰悪', '種族', 'そう', '書生', 'の', '我々', '話', '当時', 
'何', '考', '彼', '掌', 'スー', '時'
"""