import xml.etree.ElementTree as ET
import pydot_ng as pydot

def _57():
    
    root = ET.parse("nlp.txt.xml")

    for sentence in root.iterfind("./document/sentences/sentence"):
        sent_id = int(sentence.get("id"))

        edges = []

        for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):

            # 句点除去 
            if dep.get('type') != 'punct':

                govr = dep.find('./governor')
                dept = dep.find('./dependent')
                edges.append(((govr.get('idx'), govr.text), (dept.get('idx'), dept.text)))
            
        graph = pydot.Dot(graph_type='digraph')

        for node in edges:
            id0,lavel0 = node[0]
            id1,lavel1 = node[1]
            graph.add_node(pydot.Node(id0,label=lavel0))
            graph.add_node(pydot.Node(id1,label=lavel1))
            graph.add_edge(pydot.Edge(id0, id1))

        graph.write_png("57-{}.png".format(sent_id))

if __name__ == "__main__":
    _57()
