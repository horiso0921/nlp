col1 = []
col2 = []
with open("hightemp.txt",encoding="utf-8") as f:
    for line in f:
        words = line.split("\t")
        col1.append(words[0]+"\n")
        col2.append(words[1]+"\n")

with open("col1.txt", mode="w", encoding="utf-8") as f:
    f.write("".join(col1))

with open("col2.txt", mode="w", encoding="utf-8") as f:
    f.write("".join(col2))

# 結果確認
# diff <(cat col1.txt) <(cut -f1 hightemp.txt)
# diff <(cat col2.txt) <(cut -f2 hightemp.txt)
