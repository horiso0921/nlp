def n_gram(target, n):
    # 基準を1文字(単語)ずつずらしながらn文字分抜き出す
    res = []
    for i in range(len(target) - n + 1):
        res.append("".join([target[i + j] for j in range(n)]))
    return res

Target1 = "paraparaparadise"
Target2 = "paragraph"
X= set(n_gram(Target1, 2))
Y = set(n_gram(Target2, 2))

# 和集合
print(X | Y)

# 積集合
print(X & Y)

# 差集合
print(X - Y)

# seが両方に含まれるか
print("Yes" if "se" in X & Y else "No")