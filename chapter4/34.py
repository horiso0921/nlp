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

def _34():

    morpheme_dict_lists = get_morpheme_dict_lists()

    noun_phrase_list = []

    for line in morpheme_dict_lists:
        for index, word in enumerate(line[1:-1],start=1):
            preword = line[index-1]
            postword = line[index+1]
            if preword["pos"] == postword["pos"] == "名詞" and word["surface"] == "の":
                noun_phrase = preword["surface"] + word["surface"] + postword["surface"]
                noun_phrase_list.append(noun_phrase)

    print(noun_phrase_list)
if __name__ == "__main__":
    _34()