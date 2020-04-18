from random import sample
def shuffleWordsFromSecondToSecondFromTheLast(target):
    res = []
    for word in target.split():
        if len(word) <= 4:
            res.append(word)
        else:
            res.append(word[0] +
                "".join(sample(word[1:-1], len(word) - 2)) + word[-1])
    return " ".join(res)


Sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(shuffleWordsFromSecondToSecondFromTheLast(Sentence))