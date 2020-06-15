import re
def _51():
    with open("50") as f:
        contents = []
        for line in f:
            line = line.replace(" ", "\n")
            line = re.sub(r"[^a-zA-Z0-9\n]","",line)
            if line:
                contents.append(line)
        print("\n".join(contents))

if __name__ == "__main__":
    _51()

"""
Natural
language
processing

From
Wikipedia
the
free
encyclopedia

Natural
language
processing
NLP
is
a
field
of
computer
science
"""