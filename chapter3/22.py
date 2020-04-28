import re

input_f_name = "contents.txt"
output_f_name = "out22.txt"
pattern = r"\[\[Category:([^\|]*)\|?(.*)\]\]"

def _22():
    with open(input_f_name, encoding="utf-8") as target:
        with open(output_f_name, "w", encoding="utf-8") as output_f:
            for line in target:
                categories = re.search(pattern, line)
                if categories:
                    output_f.write(re.sub(pattern, r"\1",line))
            
if __name__ == "__main__":
    _22()