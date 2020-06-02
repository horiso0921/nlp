from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from morpheme import get_morpheme_dict_lists

def _39():

    morpheme_dict_lists = get_morpheme_dict_lists()

    words = defaultdict(int)
    for line in morpheme_dict_lists:
        for word in line:
            if word["pos"] != "記号":
                words[word["base"]] += 1
    

    # baseがうまく認識しないから*になってるものが多いよ...
    items = sorted(words.items(), key=lambda x: -x[1])
    counts = list(map(lambda x: x[1], items))

    # 散布図のデータ指定
    plt.scatter(range(1, len(counts) + 1),counts)

    # 軸の値の範囲の調整
    plt.xlim(1, len(counts) + 1)
    plt.ylim(1, counts[0])

    # 対数グラフに
    plt.xscale('log')
    plt.yscale('log')

    # 表示
    plt.show()

if __name__ == "__main__":
    _39()