import re

input_f_name = "contents.txt"
output_f_name = "out23.txt"
pattern = r"={2,4}[^=]*={2,4}"

def _23():
    with open(input_f_name, encoding="utf-8") as target:
        with open(output_f_name, "w", encoding="utf-8") as output_f:
            for line in target:
                section = re.search(pattern, line)
                if section:
                    output_f.write("{} {}\n".format(line.rstrip(),line.count("=") // 2 - 1))
            
if __name__ == "__main__":
    _23()