import xml.etree.ElementTree as ET

def _55():
    
    root = ET.parse("nlp.txt.xml")

    for token in root.iter("token"):

        word = token.findtext("word")
        ner = token.findtext("NER")
        if ner == "PERSON":
            print(word)

if __name__ == "__main__":
    _55()


"""
Alan
Turing
Joseph
Weizenbaum
MARGIE
Schank
Wilensky
Meehan
Lehnert
Carbonell
Lehnert
Racter
Jabberwacky
Moore
"""