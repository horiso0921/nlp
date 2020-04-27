import gzip
import json

with gzip.open("jawiki-country.json.gz", "rt") as target:
    for line in target:
        file_content = json.loads(line)
        if file_content['title'] == "イギリス":
            print(file_content['text'])
        
