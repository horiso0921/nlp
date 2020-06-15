from morph import Morph

class Chunk(object):
    
    __slots__ = ["_morphs", "dst", "srcs"]

    def __init__(self, dst: int):
    
        self._morphs = []
        self.dst = dst
        self.srcs = []
    

    @property 
    def morphs(self):
        return self._morphs

    def chunkcontents(self):
        return "{} {} {}".format("".join(map(lambda x: x.surface, self._morphs)), self.dst, self.srcs)

    def append_srcs(self, src: int):
        self.srcs.append(src)

    def append_morphs(self, morph: Morph):
        self._morphs.append(morph)


def make_all_sentences_chunks_list(fname):

    # 全文におけるchunksをまとめるlist
    contents = []

    # ある文におけるchunkをまとめるlist
    chunks = []

    with open(fname,encoding="utf-8") as target:
    
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

    return contents