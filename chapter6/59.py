import xml.etree.ElementTree as ET
import re
ans = []

def parser(sentence):
    """
    方針
    (の数と )の数が同じになったらその深さのタグがNPならglobalのansに単語を追加する
    param : str
    """
    global ans

    nest = 0
    for i, s in enumerate(sentence):
        if s  == " ":
            pre = i + 1
            tag = sentence[1:i]
            break
    word = []
    blanc = pre
    f = 0


    for i,node in enumerate(sentence[pre:],start=pre):
        if node == "(":
            if nest == 0:
                pre = i
            nest += 1
        elif node == ")":
            nest -= 1
            if f:
                f = 0
                word.append(sentence[blanc+1:i])
            if not nest: 
                parser(sentence[pre:i+1]) 
        elif node == " ":
            blanc = i
        elif blanc + 1 == i and node != "(":
            f = 1

    if tag == "NP":
        ans.append(" ".join(word))

def _59():
    
    global ans

    root = ET.parse("nlp.txt.xml")

    for sentence in root.iterfind("./document/sentences/sentence/parse"):
        parser(sentence.text)
        ans.append(" === Sentence Changed === ")
    print("\n".join(ans))

if __name__ == "__main__":
    _59()

"""
 === Sentence Changed === 
Natural language processing
Wikipedia
the free encyclopedia
Natural language processing
NLP
the free encyclopedia Natural language processing -LRB- NLP -RRB-
a field
computer science
artificial intelligence
linguistics
the interactions
computers
human -LRB- natural -RRB- languages
computers and human -LRB- natural -RRB- languages
the interactions between computers and human -LRB- natural -RRB- languages
linguistics concerned with the interactions between computers and human -LRB- natural -RRB- languages
computer science , artificial intelligence , and linguistics concerned with the interactions between computers and human -LRB- natural -RRB- languages
a field of computer science , artificial intelligence , and linguistics concerned with the interactions between computers and human -LRB- natural -RRB- languages
 === Sentence Changed === 
NLP
the area
humani - computer interaction
the area of humani - computer interaction
 === Sentence Changed === 
Many challenges
NLP
Many challenges in NLP
natural language understanding
that
enabling computers
"""