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
                print("\t".join(value))              


if __name__ == "__main__":
    _58()

"""
involve	challenges	understanding
is	that	computers
involve	others	generation
published	Turing	article
involved	experiment	translation
provided	ELIZA	interaction
exceeded	patient	base
provide	ELIZA	response
structured	which	information
discouraged	underpinnings	sort
underlies	that	approach
produced	algorithms	systems
introduced	Part	use
make	which	decisions
contains	input	errors
involved	implementations	coding
take	algorithms	set
produced	algorithms	systems
make	which	decisions
have	models	advantage
express	they	certainty
make	procedures	use
make	that	decisions
"""