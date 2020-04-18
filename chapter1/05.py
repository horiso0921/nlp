def n_gram(target, n):
    # 基準を1文字(単語)ずつずらしながらn文字分抜き出す
    return ["".join((target[i + j] for j in range(n))) for i in range(len(target) - n + 1)]

Sentence = "I am an NLPer"
Words = Sentence.split()
print(n_gram(Words, 2))
print(n_gram(Sentence, 2))
