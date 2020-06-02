from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

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

def _39():

    morpheme_dict_lists = get_morpheme_dict_lists()

    words = defaultdict(int)
    for line in morpheme_dict_lists:
        for word in line:
            if word["pos"] not in  ("記号","助動詞","助詞"):
                words[word["base"]] += 1
    

    # baseがうまく認識しないから*になってるものが多いよ...
    items = sorted(words.items(), key=lambda x: -x[1])
    counts = list(map(lambda x: x[1], items))

    # グラフで使うフォント情報(デフォルトのままでは日本語が表示できない)
    fp = FontProperties(fname="C:\\Windows\\Fonts\\meiryo.ttc")


    # 散布図のデータ指定
    plt.scatter(range(1, len(counts) + 1),counts)

    # 軸の値の範囲の調整
    plt.xlim(1, len(counts) + 1)
    plt.ylim(1, counts[0])

    # 対数グラフに
    plt.xscale('log')
    plt.yscale('log')

    # グラフのタイトル、ラベル指定
    plt.title("39. Zipfの法則", fontproperties=fp)
    plt.xlabel('出現度順位', fontproperties=fp)
    plt.ylabel('出現頻度', fontproperties=fp)

    # グリッドを表示
    plt.grid(axis='both')

    # 表示
    plt.show()

if __name__ == "__main__":
    _39()