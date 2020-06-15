import re
import xml.etree.ElementTree as ET

def _53():
    
    root = ET.parse("nlp.txt.xml")

    for word in root.iter("word"):
        print(word.text)

if __name__ == "__main__":
    _53()


"""
Natural
language
processing
From
Wikipedia
,
the
free
encyclopedia
Natural
language
processing
(
NLP
)
is
a
field
of
computer
"""