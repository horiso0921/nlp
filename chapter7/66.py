from pymongo import MongoClient

def _66():
    count = 0
    with MongoClient('mongodb://localhost:27017/') as client:
        assert client is not None
        db = client.testdb
        collection = db.artist

        for _ in collection.find({"area":"Japan"}):
            count += 1
    print(count)
if __name__ == "__main__":
    _66()
"""
> use testdb
switched to db testdb
> db.getCollection("artist").find({'area': 'Japan'}).count()
22821
"""

"""
22821
"""