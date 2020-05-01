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

def _37():

    morpheme_dict_lists = get_morpheme_dict_lists()

    words = defaultdict(int)
    for line in morpheme_dict_lists:
        for word in line:
            if word["pos"] not in  ("記号","助動詞","助詞"):
                words[word["base"]] += 1
    

    # baseがうまく認識しないから*になってるものが多いよ...
    items = sorted(words.items(), key=lambda x: -x[1])
    words = items

    # 頻度上位10語の取得
    size = 10
    list_word = words[:size]
    print(list_word)

    # 単語（x軸用）と出現数（y軸用）のリストに分解
    list_zipped = list(zip(*list_word))
    words = list_zipped[0]
    counts = list_zipped[1]

    # グラフで使うフォント情報(デフォルトのままでは日本語が表示できない)
    fp = FontProperties(
        fname="C:\\Windows\\Fonts\\meiryo.ttc"
    )

    # 棒グラフのデータ指定
    plt.bar(
        range(0, size),		# x軸の値（0,1,2...9）
        counts,				# それに対応するy軸の値
        align='center'		# x軸における棒グラフの表示位置
    )

    # x軸のラベルの指定
    plt.xticks(
        range(0, size),		# x軸の値（0,1,2...9）
        words,				# それに対応するラベル
        fontproperties=fp	# 使うフォント情報
    )

    # x軸の値の範囲の調整
    plt.xlim(
        xmin=-1, xmax=size	# -1〜10（左右に1の余裕を持たせて見栄え良く）
    )

    # グラフのタイトル、ラベル指定
    plt.title(
        '37. 頻度上位10語',	# タイトル
        fontproperties=fp	# 使うフォント情報
    )
    plt.xlabel(
        '出現頻度が高い10語',# x軸ラベル
        fontproperties=fp	# 使うフォント情報
    )
    plt.ylabel(
        '出現頻度',			# y軸ラベル
        fontproperties=fp	# 使うフォント情報
    )

    # グリッドを表示
    plt.grid(axis='y')

    # 表示
    plt.show()

if __name__ == "__main__":
    _37()