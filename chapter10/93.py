def _93():
    fname_list = ["92","92_85"]

    with open("93", "w") as out:
        for fname in fname_list:
            with open(fname, "r") as target:
                total = 0
                correct = 0

                for line in target:
                    word = line.rstrip().split()
                    total += 1
                    correct += word[3] == word[4]
            
            print(f"{fname} : {correct / total} : correct = {correct}, total {total}", file=out)

if __name__ == "__main__":
    _93()
"""
92 : 0.6640316205533597 : correct = 336, total 506
92_85 : 0.029644268774703556 : correct = 15, total 506
"""