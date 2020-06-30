import leveldb

FNAME_DB = "sample_DB"

def _61():
    db = leveldb.LevelDB(FNAME_DB)
    print("please input artist name (If you input only enter, I choose Green Day)")
    artist_name = input(">")
    if artist_name == "":
        artist_name = "Green Day"
    out = []
    for key, value in db.RangeIter(key_from=(artist_name+"(").encode()):
        name,id = key.decode().split("(id=")
        
        if name!= artist_name:
            break

        out.append(name+"(id="+str(id)+"'s area is "+value.decode())
    
    if out:
        print("\n".join(out))
    else:
        print(artist_name+" : No record")
if __name__ == "__main__":
    _61()

"""
please input artist name (If you input only enter, I choose Green Day)
>
SMAP(id=265728)'s area is Japan
"""