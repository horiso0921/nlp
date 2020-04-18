def n_gram(target, n):
    # 基準を1文字(単語)ずつずらしながらn文字分抜き出す
    return ["".join((target[i + j] for j in range(n))) for i in range(len(target) - n + 1)]

Target1 = "paraparaparadise"
Target2 = "paragraph"
bi_gram1 = set(n_gram(Target1, 2))
bi_gram2 = set(n_gram(Target2, 2))

# 和集合
print(bi_gram1 | bi_gram2)

# 積集合
print(bi_gram1 & bi_gram2)

# 差集合
print(bi_gram1 - bi_gram2)

# seが両方に含まれるか
print("Yes" if "se" in bi_gram1 & bi_gram2 else "No")