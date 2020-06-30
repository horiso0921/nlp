from pymongo import MongoClient
from pprint import pprint

def _67():
    with MongoClient('mongodb://localhost:27017/') as client:
        assert client is not None
        db = client.testdb
        collection = db.artist

        print("please input artist aliases name (If you input only enter, I choose Green Day)")
        artist_name = input(">")
        if artist_name == "":
            artist_name = "Green Day"

        docs = collection.find({"aliases.name":artist_name})

        if docs:
            for doc in docs:
                pprint(doc)

        else:
            print("No data")
if __name__ == "__main__":
    _67()


"""
please input artist aliases name (If you input only enter, I choose Green Day)
>{'_id': ObjectId('5ef9708bc43bea7f1f83dc36'),
 'aliases': [{'name': 'OASIS', 'sort_name': 'OASIS'},
             {'name': 'オアシス', 'sort_name': 'オアシス'}],
 'area': 'United Kingdom',
 'begin': {'year': 1991},
 'end': {'date': 28, 'month': 8, 'year': 2009},
 'ended': True,
 'gid': '39ab1aed-75e0-4140-bd47-540276886b60',
 'id': 20660,
 'name': 'Oasis',
 'rating': {'count': 13, 'value': 86},
 'sort_name': 'Oasis',
 'tags': [{'count': 1, 'value': 'rock'},
          {'count': 3, 'value': 'britpop'},
          {'count': 4, 'value': 'british'},
          {'count': 1, 'value': 'uk'},
          {'count': 1, 'value': 'britannique'},
          {'count': 1, 'value': 'rock and indie'},
          {'count': 1, 'value': 'england'},
          {'count': 1, 'value': 'manchester'}],
 'type': 'Group'}

"""