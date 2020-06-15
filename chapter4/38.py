from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from morpheme import get_morpheme_dict_lists

def _38():

    morpheme_dict_lists = get_morpheme_dict_lists()

    words = defaultdict(int)
    for line in morpheme_dict_lists:
        for word in line:
            if word["pos"] != "記号":
                words[word["base"]] += 1
    

    # baseがうまく認識しないから*になってるものが多いよ...
    counts = words.values()

    # ヒストグラムのデータ指定
    plt.hist(counts,bins=20,range=(1, 20))		

    # x軸の値の範囲の調整
    plt.xlim(xmin=1, xmax=20)

    # 表示
    plt.show()
8

if __name__ == "__main__":
    _38()