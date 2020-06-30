import json
import leveldb
from collections import defaultdict

FNAME = "artist.json"
FNAME_DB = "sample_DB"

def _60():
    d = defaultdict(int)
    with open(FNAME,"r",encoding="UTF-8") as target:
        for line in target:
            data_json = json.loads(line)

            # 注意点
            # NAMEの重複とareaがないやつもある
            # 重複はID を付けて識別
            # areaがないものはgetを使うことで無を取得するようにした
            for t in data_json.get("tags",[]):
                d[t["value"]] += 1
    
    l = sorted(d.items(), key=lambda x: -x[1])
    print(l[:30])


if __name__ == "__main__":
    _60()