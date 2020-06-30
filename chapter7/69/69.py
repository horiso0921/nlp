
from flask import Flask, render_template, request
from pymongo import MongoClient
from pprint import pprint
from collections import defaultdict
import pymongo

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/searched',methods=["POST"])
def searched():
    clue = defaultdict(str)
    form_contents = request.form
    if form_contents["artist_name"]:
        artist_name = request.form["artist_name"]
        clue["name"] = artist_name
    if form_contents["alias"]:
        alias = request.form["alias"]
        clue["aliases.name"] = alias
    if form_contents["tag"]:
        tag = request.form["tag"]
        clue["tags.value"] = tag
    cl = clue
    if len(clue.items()) >= 2:
        tmp = []
        for key,value in clue.items():
            tmp.append({key: value})
        clue = {"$and":tmp}
    with MongoClient('mongodb://localhost:27017/') as client:
        assert client is not None
        db = client.testdb
        collection = db.artist
        results = collection.find(clue)
        results.sort('rating.count', pymongo.DESCENDING)
        total = results.count()
        responses = results[:10]
    res = []
    for r in responses:
        t = {}
        if "aliases" in r:
            t["aliases"] = r["aliases"][0]["name"]
        else:
            t["aliases"] = "*No Data"
        if "name" in r:
            t["name"] = r["name"]
        else:
            t["name"] = "*No Data"
        if "tags" in r:
            t["tags"] = r["tags"]
        else:
            t["tags"] = "*No Data"
        if "begin" in r:
            t["begin"] = r["begin"]["year"]
        else:
            t["begin"] = "*No Data"
        res.append(t)
    print(form_contents,clue)
    return render_template("searched.html", r=res,clue=cl.values(), a=total)

## おまじない
if __name__ == "__main__":
    app.run(port=8080, debug=True)