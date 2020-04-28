import re

input_f_name = "contents.txt"
output_f_name = "out25.txt"
pattern = r"\[\[File:([^\|]*).*\]\]"

def _24():
    with open(input_f_name, encoding="utf-8") as target:
        with open(output_f_name, "w", encoding="utf-8") as output_f:
            for line in target:
                mediaFile = re.search(pattern, line)
                if mediaFile:
                    output_f.write(re.sub(pattern, r"\1",line))
            
if __name__ == "__main__":
    _24()