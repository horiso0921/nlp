class Morph(object):

    __slots__ = ["surface", "base", "pos", "pos1"]

    def __init__(self, line: str):
        
        word, feature_str = line.split("\t")

        features = feature_str.split(",")

        self.surface = word
        self.base =  features[6]
        self.pos = features[0]
        self.pos1 = features[1]

    def print_allvariable(self):
        print("surface : {} , base : {} , pos : {} , pos1 : {}".format(self.surface,self.base,self.pos,self.pos1))
        return