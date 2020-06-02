from morpheme import get_morpheme_dict_lists

def _35():

    morpheme_dict_lists = get_morpheme_dict_lists()

    nouns = []
    tmp_nouns = []
    for line in morpheme_dict_lists:
        for word in line:
            if word["pos"] == "名詞":
                tmp_nouns.append(word["surface"])
            else:
                if len(tmp_nouns) >= 2:
                    nouns.append("".join(tmp_nouns))
                tmp_nouns = []

    if len(tmp_nouns) >= 2:
        nouns.append("".join(tmp_nouns))

    # ここで気づいたけど many a slip 'twixt the cup and the lipが全部英語になってる（解決わからず） 
    print(nouns)

if __name__ == "__main__":
    _35()


"""
'人間中', '一番獰悪', '時妙', '一毛', 'その後猫', 
'一度', 'ぷうぷうと煙', '邸内', '三毛', '書生以外', 
'四五遍', 'この間おさん', '三馬', '御台所', 'まま奥', 
'住家', '終日書斎', '勉強家', '勉強家', '勤勉家', '二三ページ', '主人以外', '限り吾輩',
"""