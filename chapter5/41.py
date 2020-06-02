from morph import Morph

class Chunk(object):
    
    __slots__ = ["morphs", "dst", "srcs"]

    def __init__(self, dst: int):
    
        self.morphs = []
        self.dst = dst
        self.srcs = []
    
    def chunkcontents(self):
        return "{} {} {}".format("".join(map(lambda x: x.surface, self.morphs)), self.dst, self.srcs)

    def append_srcs(self, src: int):
        self.srcs.append(src)

    def append_morphs(self, morph: Morph):
        self.morphs.append(morph)

def _41():

    # 全文におけるchunksをまとめるlist
    contents = []

    # ある文におけるchunkをまとめるlist
    chunks = []

    with open("neko.txt.cabocha") as target:
    
        for line in target:

            line = line.rstrip()

            # 係受け行かどうか
            if line[0] == "*" and len(line.split()) == 5:
                
                # 係受けなら解析するchunk(文節)インスタンスを生成してchunksに参照を渡しておく
                chunk = Chunk(int(line.split()[2][:-1]))
                chunks.append(chunk)

            # 文末かどうか
            elif line == "EOS" or line == "":
                # 文末ならその分における文節は定義済み
                # ある文節(index=i)のdstに対して有向辺i→dstは張れているので逆辺dst→iを張る
                # この辺についてはscrsで管理する
                for i, chunk in enumerate(chunks):
                    dst = chunk.dst
                    if dst != -1:
                        chunks[dst].append_srcs(i)
                    
                contents.append(chunks)
                chunks = []
            
            else:
                # 今の文節におけるmorphを追加
                chunk.append_morphs(Morph(line))


    print("morphs : dst : srcs")
    for chunk in contents[7]:
        print(chunk.chunkcontents())


if __name__ == "__main__":
    _41()

"""
morphs : dst : srcs
吾輩は 5 []
ここで 2 []
始めて 3 [1]
人間という 4 [2]
ものを 5 [3]
見た。 -1 [0, 4]
"""