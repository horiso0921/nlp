from collections import defaultdict

prefe_dic = defaultdict(int)

with open("hightemp.txt", encoding="utf-8") as f:
    for line in f:
        prefe = line.split("\t")[0]
        prefe_dic[prefe] += 1

prefe_lis = sorted(prefe_dic.items(), key=lambda x: x[1], reverse=True)

print("\n".join(map(lambda x: x[0], prefe_lis)))
