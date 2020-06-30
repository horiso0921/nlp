from pymongo import MongoClient
import pprint

def _65():
    with MongoClient('mongodb://localhost:27017/') as client:
        assert client is not None
        db = client.testdb
        collection = db.artist

        for doc in collection.find({"name":"Queen"}):
            pprint.pprint(doc)

if __name__ == "__main__":
    _65()

"""
{'_id': ObjectId('5ef9708bc43bea7f1f82f077'),
 'aliases': [{'name': 'Queen', 'sort_name': 'Queen'}],
 'area': 'Japan',
 'ended': True,
 'gender': 'Female',
 'gid': '420ca290-76c5-41af-999e-564d7c71f1a7',
 'id': 701492,
 'name': 'Queen',
 'sort_name': 'Queen',
 'tags': [{'count': 1, 'value': 'kamen rider w'},
          {'count': 1, 'value': 'related-akb48'}],
 'type': 'Character'}
{'_id': ObjectId('5ef9708bc43bea7f1f83b723'),
 'aliases': [{'name': '女王', 'sort_name': '女王'}],
 'area': 'United Kingdom',
 'begin': {'date': 27, 'month': 6, 'year': 1970},
 'ended': True,
 'gid': '0383dadf-2a4e-4d10-a46a-e9e041da8eb3',
 'id': 192,
 'name': 'Queen',
 'rating': {'count': 24, 'value': 92},
 'sort_name': 'Queen',
 'tags': [{'count': 2, 'value': 'hard rock'},
          {'count': 1, 'value': '70s'},
          {'count': 1, 'value': 'queen family'},
          {'count': 1, 'value': '90s'},
          {'count': 1, 'value': '80s'},
          {'count': 1, 'value': 'glam rock'},
          {'count': 4, 'value': 'british'},
          {'count': 1, 'value': 'english'},
          {'count': 2, 'value': 'uk'},
          {'count': 1, 'value': 'pop/rock'},
          {'count': 1, 'value': 'pop-rock'},
          {'count': 1, 'value': 'britannique'},
          {'count': 1, 'value': 'classic pop and rock'},
          {'count': 1, 'value': 'queen'},
          {'count': 1, 'value': 'united kingdom'},
          {'count': 1, 'value': 'langham 1 studio bbc'},
          {'count': 1, 'value': 'kind of magic'},
          {'count': 1, 'value': 'band'},
          {'count': 6, 'value': 'rock'},
          {'count': 1, 'value': 'platinum'}],
 'type': 'Group'}
{'_id': ObjectId('5ef9708cc43bea7f1f85717b'),
 'ended': True,
 'gid': '5eecaf18-02ec-47af-a4f2-7831db373419',
 'id': 992994,
 'name': 'Queen',
 'sort_name': 'Queen'}

"""

"""
> use testdb
switched to db testdb
> db.getCollection("artist").find({"name":"Queen"})
{ "_id" : ObjectId("5ef9708bc43bea7f1f82f077"), "name" : "Queen", "area" : "Japan", "gender" : "Female", "tags" : [ { "count" : 1, "value" : "kamen rider w" }, { "count" : 1, "value" : "related-akb48" } ], "sort_name" : "Queen", "ended" : true, "gid" : "420ca290-76c5-41af-999e-564d7c71f1a7", "type" : "Character", "id" : 701492, "aliases" : [ { "name" : "Queen", "sort_name" : "Queen" } ] }
{ "_id" : ObjectId("5ef9708bc43bea7f1f83b723"), "rating" : { "count" : 24, "value" : 92 }, "begin" : { "date" : 27, "month" : 6, "year" : 1970 }, "name" : "Queen", "area" : "United Kingdom", "tags" : [ { "count" : 2, "value" : "hard rock" }, { "count" : 1, "value" : "70s" }, { "count" : 1, "value" : "queen family" }, { "count" : 1, "value" : "90s" }, { "count" : 1, "value" : "80s" }, { "count" : 1, "value" : "glam rock" }, { "count" : 4, "value" : "british" }, { "count" : 1, "value" : "english" }, { "count" : 2, "value" : "uk" }, { "count" : 1, "value" : "pop/rock" }, { "count" : 1, "value" : "pop-rock" }, { "count" : 1, "value" : "britannique" }, { "count" : 1, "value" : "classic pop and rock" }, { "count" : 1, "value" : "queen" }, { "count" : 1, "value" : "united kingdom" }, { "count" : 1, "value" : "langham 1 studio bbc" }, { "count" : 1, "value" : "kind of magic" }, { "count" : 1, "value" : "band" }, { "count" : 6, "value" : "rock" }, { "count" : 1, "value" : "platinum" } ], "sort_name" : "Queen", "ended" : true, "gid" : "0383dadf-2a4e-4d10-a46a-e9e041da8eb3", "type" : "Group", "id" : 192, "aliases" : [ { "name" : "女 
王", "sort_name" : "女王" } ] }
{ "_id" : ObjectId("5ef9708cc43bea7f1f85717b"), "ended" : true, "gid" : "5eecaf18-02ec-47af-a4f2-7831db373419", "sort_name" : "Queen", "id" : 992994, "name" : "Queen" }
"""
