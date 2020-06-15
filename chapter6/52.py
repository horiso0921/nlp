import re
from stemming.porter2 import stem

def _52():
    with open("51") as f:
        contents = []
        for line in f:
            line = line.rstrip()
            if line:
                contents.append(line + "\t" + stem(line))
        print("\n".join(contents))

if __name__ == "__main__":
    _52()

"""
Natural	Natur
language	languag
processing	process
From	From
Wikipedia	Wikipedia
the	the
free	free
encyclopedia	encyclopedia
Natural	Natur
language	languag
processing	process
NLP	NLP
is	is
a	a
field	field
of	of
computer	comput
science	scienc
"""