res = []
with open("col1.txt", encoding="utf-8") as f:
    for line in f:
        res.append(line.rstrip())

with open("col2.txt", encoding="utf-8") as f:
    for i, line in enumerate(f):
        res[i] += "\t" + line

with open("marge.txt", "w", encoding="utf-8") as f:
    f.write("".join(res))

# 確認
# diff marge.txt <(paste col1.txt col2.txt)