fname = "81_out"
out_fname = "82_out"
import random
def _82():
    with open(fname, "r", encoding="utf-8") as target, open(out_fname,"w") as out_target:
        for line in target:
            tokens = line.rstrip().split()
            
            for i in range(len(tokens)):
                j = random.randint(1, 5)
                for k in range(1,j+1):
                    if 0 <= i + k < len(tokens):
                        print(tokens[i]+"\t"+tokens[i+k], file=out_target)
                    if 0 <= i - k < len(tokens):
                        print(tokens[i]+"\t"+tokens[i-k], file=out_target)

if __name__ == "__main__":
    _82()

"""
wc 82_out
68107469 136214938 817274454 82_out
head -10 82
Anarchism       is
is      Anarchism
is      a
is      political
is      philosophy
a       Anarchism
a       is
a       political
a       philosophy
political       Anarchism
"""