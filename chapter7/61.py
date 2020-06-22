import leveldb
import re

FNAME_DB = "sample_DB"

def _61():
    db = leveldb.LevelDB(FNAME_DB)
    print("please input artist name (If you input random, I choose random artist)")
    artist_name = input(">")
    if artist_name == "random":
        artist_name = "SMAP"
    out = []
    for key, value in db.RangeIter(key_from=artist_name.encode()):
        match = re.match(r"(.*?)\(id=(\d*)\)", key.decode())
        name,id = match.groups()
        if name!= artist_name:
            break

        out.append(name+"(id="+str(id)+")"+"'s area is "+value.decode())
    
    if out:
        print("\n".join(out))
    else:
        print(artist_name+" : No record")
if __name__ == "__main__":
    _61()

"""
please input artist name (If you input random, I choose random artist)
>random
SMAP(id=265728)'s area is Japan
"""