from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from morpheme import get_morpheme_dict_lists

def _37():

    morpheme_dict_lists = get_morpheme_dict_lists()

    words = defaultdict(int)
    for line in morpheme_dict_lists:
        for word in line:
            if word["pos"] not in  "記号":
                words[word["base"]] += 1
    

    # baseがうまく認識しないから*になってるものが多いよ...
    items = sorted(words.items(), key=lambda x: -x[1])
    words = items

    size = 10
    list_word = words[:size]
    print(list_word)

    # 単語（x軸用）と出現数（y軸用）のリストに分解
    list_zipped = list(zip(*list_word))
    words = list_zipped[0]
    counts = list_zipped[1]

    # グラフで使うフォント情報(デフォルトのままでは日本語が表示できない)
    fp = FontProperties(fname="C:\\Windows\\Fonts\\meiryo.ttc")

    # 棒グラフのデータ指定
    plt.bar(range(0, size),counts)

    # x軸のラベルの指定
    plt.xticks(range(0, size),words,fontproperties=fp)

    # 表示
    plt.show()

if __name__ == "__main__":
    _37()