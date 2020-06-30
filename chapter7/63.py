import leveldb
import json


FNAME = "artist.json"
FNAME_DB = "DB_63"


def make_db(dic, DB_NAME, db):
    """
    leveldbのデータベースを作成する

    Parameters
    -------
    dic : dict[str, dict or str or int or list]
        データベースに保存するデータ
    DB_NAME : str
        データベースの名前
    db : leveldb
        leveldbのインスタンス
    """
    for key, value in dic.items():

        if type(value) in [dict, list]:
            db.Put(key.encode(), json.dumps(value).encode())
        else:
            db.Put(key.encode(), value.encode())


def get_data_from_json_file(fname,value, default):
    """
    fileからvalueで指定したjsonデータを取得する
    """
    docs = {}
    with open(fname,"r",encoding="UTF-8") as target:
        for line in target:
            data_json = json.loads(line)
        
            key = "{}(id={})".format(data_json["name"], str(data_json["id"]))
            values = data_json.get(value, default)

            docs[key] = values
    return docs

def generate_db_instance(fname_db, value, default):
    """
    dbインスタンスを生成する
    dbがないときはcontensから値を持ってくる
    """
    try:
        db = leveldb.LevelDB(fname_db, error_if_exists=True)
        docs = get_data_from_json_file(FNAME,value, default)
        make_db(docs, fname_db, db)
    except:
        db = leveldb.LevelDB(fname_db)
    return db

def print_artist_tags(db):
    """
    標準入力からアーティスト名を受け取って
    アーティスト名とタグを出力する
    """

    print("please input artist name (If you input only enter, I choose Green Day)")
    artist_name = input(">")
    if artist_name == "":
        artist_name = "Green Day"

    out = []
    for key, value in db.RangeIter(key_from=(artist_name+"(").encode()):
        name,id = key.decode().split("(id=")
        if name!= artist_name:
            break

        tmp = []
        tmp.append(name+"(id="+str(id))

        tags = json.loads(value.decode())
    
        for tag in tags:
            count, tag_name = tag["count"], tag["value"] 
            tmp.append(" ・ TagName : "+tag_name+ " | count : " + str(count))
        out.append("\n".join(tmp))

    if out:
        print("\n\n == artist id changed == \n\n".join(out))
    else:
        print(artist_name+" : No record")


def _63():

    db = generate_db_instance(FNAME_DB, value="tags", default=[{"count": "No data", "value":"No data"}])

    print_artist_tags(db)


if __name__ == "__main__":
    _63()

"""
please input artist name (If you input only enter, I choose Green Day)
>Oasis(id=20660)
 ・ TagName : rock | count : 1
 ・ TagName : britpop | count : 3
 ・ TagName : british | count : 4
 ・ TagName : uk | count : 1
 ・ TagName : britannique | count : 1
 ・ TagName : rock and indie | count : 1
 ・ TagName : england | count : 1
 ・ TagName : manchester | count : 1

 == artist id changed == 

Oasis(id=286198)
 ・ TagName : No data | count : No data

 == artist id changed == 

Oasis(id=377879)
 ・ TagName : morning glory | count : 1
 ・ TagName : oasis | count : 1


please input artist name (If you input only enter, I choose Green Day)
>Green Day(id=510)
 ・ TagName : pop-punk | count : 1
 ・ TagName : alternative rock | count : 1
 ・ TagName : american | count : 3
 ・ TagName : punk rock | count : 3
 ・ TagName : rock | count : 3
 ・ TagName : pop and chart | count : 1
 ・ TagName : pop punk | count : 4
 ・ TagName : pop/rock | count : 1
 ・ TagName : américain | count : 1
 ・ TagName : usa | count : 2
 ・ TagName : punk | count : 2
 ・ TagName : punk pop | count : 1
 ・ TagName : united states | count : 1
 ・ TagName : ska punk | count : 1
 ・ TagName : california | count : 1
 ・ TagName : california punk | count : 1
 ・ TagName : classic pop punk | count : 1
 ・ TagName : classic punk | count : 1
 ・ TagName : bay area | count : 1
 ・ TagName : bay area punk | count : 1
 ・ TagName : pop | count : 2
"""