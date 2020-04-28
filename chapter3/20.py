import gzip
import json
input_f_name ="jawiki-country.json.gz"
output_f_name = "contents.txt"

def _20():
    with gzip.open(input_f_name, "rt", encoding="utf-8") as target:
        for line in target:
            file_content = json.loads(line)
            if file_content['title'] == "イギリス":
                with open(output_f_name, "w", encoding="utf-8") as output_f:
                    output_f.write(file_content['text'])
            
if __name__ == "__main__":
    _20()