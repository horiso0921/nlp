import json
import leveldb

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

if __name__ == "__main__":
    make_db()