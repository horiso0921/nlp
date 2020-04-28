import re

input_f_name = "contents.txt"
output_f_name = "out21.txt"
pattern = r"\[\[Category:.*\]\]"

def _21():
    with open(input_f_name, encoding="utf-8") as target:
        with open(output_f_name, "w", encoding="utf-8") as output_f:
            for line in target:
                if re.match(pattern, line):
                    output_f.write(line)

if __name__ == "__main__":
    _21()