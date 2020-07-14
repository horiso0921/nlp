from collections import defaultdict
import pprint

def _75():
    W = defaultdict(float)
    with open("73", "r", encoding="latin_1") as target:
        for line in target:
            word, label = line.rstrip().split()
            W[word] = float(label) 
    height_features = sorted(W.items(), key=lambda x: abs(x[1]), reverse=True)[:10]
    low_features = sorted(W.items(), key=lambda x: abs(x[1]))[:10]

    print("Top 10 : Height_Features")
    pprint.pprint(height_features)
    print("=========================")
    print("Top 10 : Low_Features")
    pprint.pprint(low_features)


if __name__ == "__main__":
    _75()

"""
Top 10 : Height_Features
[('bad', -1.4205151647476624),
 ('dull', -1.3290908173415172),
 ('bore', -1.2495817060535688),
 ('beauti', 1.0434998069468586),
 ('lack', -1.0412689934725936),
 ('fail', -1.0261076787282375),
 ('enjoy', 0.9508470843355764),
 ('worst', -0.9078420298807504),
 ('cinema', 0.8969800195845934),
 ('best', 0.8702094775410484)]
=========================
Top 10 : Low_Features
[('hammi', 8.486340159069572e-06),
 ('weakest', -3.224534256005343e-05),
 ('curs', -3.626697410186869e-05),
 ('harangu', 7.61306064942062e-05),
 ('garner', 7.848159793743051e-05),
 ('begin', -8.566226430014104e-05),
 ('doorstep', 0.00010049627807486201),
 ('hundr', 0.00010361025324587942),
 ('r-rate', 0.00011430967983602769),
 ('bright', -0.00012036501907799688)]
"""