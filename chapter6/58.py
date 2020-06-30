import xml.etree.ElementTree as ET
from collections import defaultdict

class MyDefaultdict(dict):
    def __init__(self, func):
        self.func = func
    def __getitem__(self, item):
        if item not in self:
            self[item] = self.func(item)
        return super().__getitem__(item)

def _58():

    # Stanfordnlpの出力の設定の関係でなぜかdobjタグがなかったのでobjタグで代用した
    
    root = ET.parse("nlp.txt.xml")
    SELECT_DEP_TYPE = {"nsubj": 1, "obj": 2 }

    for sentence in root.iterfind("./document/sentences/sentence"):
        
        out = MyDefaultdict(lambda x: [x[1], '', ''])

        for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):

            dep_type = dep.get('type')
            if dep_type in SELECT_DEP_TYPE:

                govr = dep.find('./governor')
                dept = dep.find('./dependent')

                out[(govr.get("idx"),govr.text)][SELECT_DEP_TYPE[dep_type]] = dept.text

        for value in out.values():
            if value[1] and value[2]:
                print("\t".join([value[1]]+value[::2]))              


if __name__ == "__main__":
    _58()

"""
challenges	involve	understanding
that	is	computers
others	involve	generation
Turing	published	article
experiment	involved	translation
ELIZA	provided	interaction
patient	exceeded	base
ELIZA	provide	response
which	structured	information
underpinnings	discouraged	sort
that	underlies	approach
algorithms	produced	systems
Part	introduced	use
which	make	decisions
input	contains	errors
implementations	involved	coding
algorithms	take	set
algorithms	produced	systems
which	make	decisions
models	have	advantage
"""