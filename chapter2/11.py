with open("hightemp.txt", encoding="utf-8") as fp:
    for data in fp:
        print(" ".join(data.split("\t")), end="")
        
# 確認
# diff <(python3 11.py) <(cat hightemp.txt | tr "\t" " ")