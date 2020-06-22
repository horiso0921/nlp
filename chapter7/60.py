import json
import leveldb

FNAME = "artist.json"
FNAME_DB = "sample_DB"

def _60():
    db = leveldb.LevelDB(FNAME_DB)
    with open(FNAME,"r",encoding="UTF-8") as target:
        for line in target:
            data_json = json.loads(line)

            # 注意点
            # NAMEの重複とareaがないやつもある
            # 重複はID を付けて識別
            # areaがないものはgetを使うことで無を取得するようにした
            key = "{}(id={})".format(data_json["name"], str(data_json["id"]))
            value = data_json.get("area", " ")
            db.Put(key.encode(), value.encode())

if __name__ == "__main__":
    _60()