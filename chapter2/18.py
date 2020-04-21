res = []

with open("hightemp.txt", encoding="utf-8") as f:
    for line in f:
        res.append(line.rstrip().split("\t"))

# 3項目目で降順ソート
res = sorted(res, key=lambda x: x[2], reverse=True)

# 各行の項目をタブで結合
res = map(lambda x: "\t".join(x), res)

# 出力
print("\n".join(res))

# 確認
# diff <(python3 18.py) <(sort -k3r -t$'\t'  hightemp.txt)