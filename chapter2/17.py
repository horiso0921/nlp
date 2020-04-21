res = set()

with open("hightemp.txt",encoding="utf-8") as f:
    for line in f:
        res.add(line.split("\t")[0])

print("\n".join(sorted(res)))

# 確認
# diff <(cut -f1 hightemp.txt | sort -u) <(python3 17.py)