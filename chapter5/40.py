class Morph(object):

    __slots__ = ["surface", "base", "pos", "pos1"]

    def __init__(self, line: str):
        
        word, feature_str = line.split("\t")

        features = feature_str.split(",")

        self.surface = word
        self.base =  features[6]
        self.pos = features[0]
        self.pos1 = features[1]

    def print_allvariable(self):
        print("surface : {} , base : {} , pos : {} , pos1 : {}".format(self.surface,self.base,self.pos,self.pos1))
        return

def _40():

    contents = []
    
    # 一文を格納するlist
    sentences = []

    with open("neko.txt.cabocha") as target:
        
        for line in target:

            line = line.rstrip()


            # EOSか最終行なら一文をresに追加
            if line == "EOS" or line == "":
                if sentences: contents.append(sentences)
                sentences = []

            # \tがないなら何もしない
            if not "\t" in line: continue

            sentences.append(Morph(line))
    
    for sent in contents[2]:
        sent.print_allvariable()

if __name__ == "__main__":
    _40()

"""
cabocha -f1 neko.txt -o neko.txt.cabocha
"""

"""
surface : 名前 , base : 名前 , pos : 名詞 , pos1 : 一般
surface : は , base : は , pos : 助詞 , pos1 : 係助詞
surface : まだ , base : まだ , pos : 副詞 , pos1 : 助詞類接続
surface : 無い , base : 無い , pos : 形容詞 , pos1 : 自立
surface : 。 , base : 。 , pos : 記号 , pos1 : 句点
"""