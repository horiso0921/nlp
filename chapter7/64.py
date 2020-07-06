from pymongo import MongoClient
import pymongo
import json
"""
pymongのドキュメント
https://api.mongodb.com/python/3.3.0/tutorial.html
"""

FNAME = "artist.json"

def _64():
    with MongoClient('mongodb://localhost:27017/') as client:
        assert client is not None
        db = client.testdb
        collection = db.artist

        docs = []

        with open(FNAME,"r",encoding="UTF-8") as target:
            for line in target:
                data = json.loads(line)
                docs.append(data)

        collection.insert_many(docs)
        
        collection.create_index("name")  
        collection.create_index("aliases.name")  
        collection.create_index("tags.value")
        collection.create_index("rating.value")
        print(len(docs))

if __name__ == "__main__":
    _64()

"""
921337
"""