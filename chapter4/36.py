from collections import defaultdict
from morpheme import get_morpheme_dict_lists

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