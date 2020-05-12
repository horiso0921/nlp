import re

input_f_name = "contents.txt"
output_f_name = "out24.txt"
pattern = r"\[\[File:([^\|]*)"

def _24():
    with open(input_f_name, encoding="utf-8") as target:
        with open(output_f_name, "w", encoding="utf-8") as output_f:
            for line in target:
                mediaFiles = re.findall(pattern, line)
                if mediaFiles:
                    for mediaFile in mediaFiles:    
                        output_f.write(mediaFile+"\n")
            
if __name__ == "__main__":
    _24()