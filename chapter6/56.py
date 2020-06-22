import xml.etree.ElementTree as ET
from collections import defaultdict

def _56():
    
    root = ET.parse("nlp.txt.xml")

    replace_dic = defaultdict(int)

    for coref in root.iterfind(".document/coreference/coreference"):

        replace = coref.findtext("./mention[@representative='true']/text")
        
        for mention in coref.iterfind("./mention"):
            if mention.get("representative", "false") == "false":

                id = int(mention.findtext("sentence"))
                start = int(mention.findtext("start"))
                end = int(mention.findtext("end"))

                if not replace_dic[(id, start)]:
                    replace_dic[(id, start)] = (end, replace)

    contents = []

    for sentence in root.iterfind("./document/sentences/sentence"):
        sent_id = int(sentence.get("id"))       
        org_rest = 0                            
        sentence_textlist = []

        for token in sentence.iterfind("./tokens/token"):
            token_id = int(token.get("id"))
            word = []

            if org_rest == 0 and replace_dic[(sent_id, token_id)]:

                (end, rep_text) = replace_dic[(sent_id, token_id)]

                word.append( "「" + rep_text + "」（")
                org_rest = end - token_id       

            word.append(token.findtext("word"))

            if org_rest:
                org_rest -= 1
                if org_rest == 0:
                    word.append("）")

            word_text = "".join(word)
            sentence_textlist.append(word_text)
        
        contents.append(" ".join(sentence_textlist))

    print("\n".join(contents))

if __name__ == "__main__":
    _56()

"""
Natural language processing From Wikipedia , the free encyclopedia Natural language processing ( NLP ) is 「the free encyclopedia Natural language processing ( NLP )」（a field of computer science , artificial intelligence , and linguistics concerned with the interactions between computers and human ( natural ) languages） .
As such , NLP is related to the area of humani - computer interaction .
Many challenges in NLP involve natural language understanding , 「Many challenges in NLP」（that） is , enabling computers to derive meaning from human or natural language input , and others involve natural language generation .
History The history of NLP generally starts in the 1950s , although work can be found from earlier periods .
In 1950 , Alan Turing published an article titled " Computing Machinery and Intelligence " which proposed what is now called the 「Alan Turing」（Turing） test as a criterion of intelligence .
The Georgetown experiment in 1954 involved fully automatic translation of more than sixty Russian sentences into English .
The authors claimed that within three or five years , 「a solved problem」（machine translation） would be a solved problem .
However , real progress was much slower , and after the ALPAC report in 1966 , which found that ten year long research had failed to fulfill the expectations , funding for 「a solved problem」（machine translation） was dramatically reduced .
Little further research in 「a solved problem」（machine translation） was conducted until the late 1980s , when the first statistical machine translation systems were developed .
「SHRDLU」（Some notably successful NLP systems developed in the 1960s） were 「SHRDLU」（SHRDLU , a natural language system working in restricted " blocks worlds " with restricted vocabularies , and ELIZA , a simulation of a Rogerian psychotherapist , written by Joseph Weizenbaum between 1964 to 1966） .
"""