import random
"""
utf-8だと読み込めない文字コードがある
latin_1にしないとダメみたい
"""

def _70():
    content = []
    with open("rt-polaritydata/rt-polarity.pos", "r", encoding="latin_1") as target:
        for line in target:
            content.append("+1 "+line.rstrip())
    with open("rt-polaritydata/rt-polarity.neg", "r", encoding="latin_1") as target:
        for line in target:
            content.append("-1 "+line.rstrip())
    random.shuffle(content)

    with open("sentiment.txt", "w", encoding="latin_1") as target:
        target.write("\n".join(content))
    
    pos = 0
    neg = 0

    with open("sentiment.txt", "r", encoding="latin_1") as target:
        for line in target:
            if line.startswith("+1"): pos += 1
            elif line.startswith("-1"): neg += 1
    print("pos :", pos,"neg :", neg)
            
    
if __name__ == "__main__":
    _70()

"""
pos : 5331 neg : 5331
"""