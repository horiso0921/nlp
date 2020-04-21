import sys

line_limit = int(sys.argv[1])
res = []

with open("hightemp.txt", encoding="utf-8") as f:
    for line in f:
        res.append(line.rstrip())

print("\n".join(res[-line_limit:]))


# 確認
# diff <(python3 15.py 10) <(tail -n 10 hightemp.txt)