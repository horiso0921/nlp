import sys

line_limit = int(sys.argv[1])

with open("hightemp.txt", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i >= line_limit:
            break
        print(line.rstrip())

# 確認
# diff <(python3 14.py 10) <(head -n 10 hightemp.txt)