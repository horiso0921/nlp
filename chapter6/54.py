import re
import xml.etree.ElementTree as ET

def _54():
    
    root = ET.parse("nlp.txt.xml")

    for token in root.iter("token"):

        word = token.findtext("word")
        lemma = token.findtext("lemma")
        pos = token.findtext("POS")

        print("{}\t{}\t{}".format(word, lemma, pos))
if __name__ == "__main__":
    _54()


"""
Natural	natural	JJ
language	language	NN
processing	processing	NN
From	from	IN
Wikipedia	Wikipedia	NNP
,	,	,
the	the	DT
free	free	JJ
encyclopedia	encyclopedia	NN
Natural	natural	JJ
language	language	NN
processing	processing	NN
(	(	-LRB-
NLP	nlp	NN
)	)	-RRB-
is	be	VBZ
a	a	DT
field	field	NN
of	of	IN
computer	computer	NN
"""