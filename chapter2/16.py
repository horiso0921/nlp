import sys

limit_lines = int(sys.argv[1])

res = []

with open("hightemp.txt",encoding="utf-8") as f:
    for line in f:
        res.append(line.rstrip())

for i in range((len(res) - 1) // limit_lines + 1):
    out_f_name = "out-"+"{:03d}".format(i+1)
    with open(out_f_name, "w", encoding="utf-8") as f:
        out_lines = res[i * limit_lines : (i + 1) * limit_lines]
        f.write("\n".join(out_lines))