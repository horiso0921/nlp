import math
from train import train
from nltk import stem
from nltk.corpus import stopwords
from collections import defaultdict
STOP_WORDS = stopwords.words('english')


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

def checkstopwords(word):
    """
    >>> checkstopwords("i")
    True
    >>> checkstopwords("me")
    True
    >>> checkstopwords("won")
    True
    >>> checkstopwords("point")
    False
    >>> checkstopwords("cabocha")
    False
    """
    return word.lower() in STOP_WORDS



def _78():
    stemmer = stem.PorterStemmer()
    contents = []
    with open("sentiment.txt", "r", encoding="latin_1") as target:
        for line in target:
            contents.append(line)
    
    block = []
    for i in range(5):
        block.append(contents[i::5])

    with open("78_train_result", "w", encoding="latin_1") as target:
        for i in range(5):
            train_lis = []
            valid_lis = block[i]
            for j in range(5):
                if i != j:
                    train_lis += block[j]
            
            W = train(train_lis)
            for line in valid_lis:
                AnsLavel, line = line[:2], line[3:]  
                line_features = []
                for word in line.split():
                    if word in ["," , "." , ":" , ";", "--", "-"]: continue
                    if not checkstopwords(word):
                        feature = stemmer.stem(word)
                        line_features.append(feature)
                a = sum(W[x] for x in line_features)
                predict = sigmoid(a)
                predict = (predict * 2) - 1

                if predict > 0:
                    lavel = "+1"
                else:
                    lavel = "-1"
                
                target.writelines(f"{AnsLavel}\t{lavel}\t{predict}\n")

    predict_posi = []
    predict_nega = []
    ans_posi = []
    ans_nega = []

    with open("78_train_result", "r", encoding="latin_1") as target:
        for line in target:
            ans, predict, _ = line.split("\t")
            if ans == "+1":
                ans_posi.append(predict)
            if ans == "-1":
                ans_nega.append(predict)
            if predict == "+1":
                predict_posi.append(ans)
            if predict == "-1":
                predict_nega.append(ans)
    
    print("--正解率--")
    accuracy = (predict_posi.count("+1") + predict_nega.count("-1")) / (len(predict_posi) + len(predict_nega))
    print(f"正解率 : {accuracy}")

    print()

    print("--適合率--")
    precision_posi = predict_posi.count("+1") / len(predict_posi)
    print(f"適合率 (肯定) : {precision_posi}")
    precision_nega = predict_nega.count("-1") / len(predict_nega)
    print(f"適合率 (否定) : {precision_nega}")

    print()

    print("--再現率--")
    recall_posi = ans_posi.count("+1") / len(ans_posi)
    print(f"再現率 (肯定) : {recall_posi}")
    recall_nega = ans_nega.count("-1") / len(ans_nega)
    print(f"再現率 (否定) : {recall_nega}")

    print()

    print("F1値")
    f1_posi = (2 * recall_posi * precision_posi) / (recall_posi + precision_posi)
    print(f"F1値（肯定）： {f1_posi}")
    f1_nega = (2 * recall_nega * precision_nega) / (recall_nega + precision_nega)
    print(f"F1値（否定）： {f1_nega}")



if __name__ == "__main__":
    _78()

"""
--正解率--
正解率 : 0.6691990245732508       

--適合率--
適合率 (肯定) : 0.6546639231824417
適合率 (否定) : 0.6867494824016563

--再現率--
再現率 (肯定) : 0.716188332395423 
再現率 (否定) : 0.6222097167510786

F1値
F1値（肯定）： 0.6840455074800681
F1値（否定）： 0.6528884952268478
"""