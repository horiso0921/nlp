from pymongo import MongoClient
from pprint import pprint
import pymongo

def _68():
    with MongoClient('mongodb://localhost:27017/') as client:
        assert client is not None
        db = client.testdb
        collection = db.artist

        docs = collection.find({"tags.value":"dance"})

        docs.sort('rating.count', pymongo.DESCENDING)

        for doc in docs[:10]:
            name = doc["name"]
            rating = doc["rating"]["count"]

            print(name+" | "+str(rating))

if __name__ == "__main__":
    _68()

"""
Madonna | 26
Björk | 23
The Prodigy | 23
Rihanna | 15
Britney Spears | 13
Maroon 5 | 11
Adam Lambert | 7
Fatboy Slim | 7
Basement Jaxx | 6
Cornershop | 5
"""