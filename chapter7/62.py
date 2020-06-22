import leveldb
import re

FNAME_DB = "sample_DB"

def _62():
    db = leveldb.LevelDB(FNAME_DB)
    ans = 0
    for _, value in db.RangeIter():
        if value.decode() == "Japan": ans += 1
    print(ans)
if __name__ == "__main__":
    _62()
"""
22821
"""