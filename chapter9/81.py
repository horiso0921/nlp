from collections import defaultdict

fname = "80_out"
country_fname = "country.txt"
out_fname = "81_out"

def _81():
    country_dict = defaultdict(defaultdict)
    with open(country_fname, "r", encoding="utf-8") as target:
        for line in target:
            line = line.rstrip()
            lis_line = line.rstrip().split()
            country_dict[len(lis_line)][line] = "_".join(lis_line)
    with open(fname, "r", encoding="utf-8") as target, open(out_fname,"w") as out_target:
        for line in target:
            tokens = line.rstrip().split()

            for i in range(1, 9):
                countrys = country_dict[i]
                for j in range(len(tokens)-i):
                    token = " ".join(tokens[j:j+i])
                    if token in countrys:
                        tokens[j:j+i] = [countrys[token]] + [""]*(i-1)
                
            print(" ".join(tokens), file=out_target)

if __name__ == "__main__":
    _81()


"""
the 1950s in the United_States  its use as a synonym is still common outside 
the United_States  On the other hand some use libertarianism to refer to individualistic 
free-market philosophy only referring to free-market anarchism as libertarian anarchism
"""