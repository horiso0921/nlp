from chunk import make_all_sentences_chunks_list
import pydot_ng as pydot

F_NAME = "neko.txt.cabocha"

def _44():
    
    contents = make_all_sentences_chunks_list(F_NAME)

    edges = []

    for sentence in contents[9:10]:
        for i, chunk in enumerate(sentence):
            if chunk.dst != -1:
                chunk_morphs = chunk.morphs
                dst_morphs = sentence[chunk.dst].morphs
                
                chunk_text_list = make_morphs_list_dispite_symbol(chunk_morphs)
                dst_text_list = make_morphs_list_dispite_symbol(dst_morphs)

                edges.append(((i, "".join(chunk_text_list)),(chunk.dst, "".join(dst_text_list))))
    
    graph = pydot.Dot(graph_type='digraph')

    for node in edges:
        id0,lavel0 = node[0]
        id1,lavel1 = node[1]
        graph.add_node(pydot.Node(id0,label=lavel0))
        graph.add_node(pydot.Node(id1,label=lavel1))
        graph.add_edge(pydot.Edge(id0, id1))

    graph.write_png("44.png")

def make_morphs_list_dispite_symbol(morphs):
    res = []
    for morph in morphs:
        if morph.pos == "記号": continue
        res.append(morph.surface)
    return res

if __name__ == "__main__":
    _44()
