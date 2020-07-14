import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
thresholds = []
accuracys = []
precisions = []
recalls = []
f1s = []


def score(threshold):
    predict_posi = []
    predict_nega = []
    ans_posi = []
    ans_nega = []

    with open("76", "r", encoding="latin_1") as target:
        for line in target:
            ans, _, predict = line.split("\t")
            predict = float(predict)
            if predict >= threshold:
                predict = "+1"
            else:
                predict = "-1"
            if ans == "+1":
                ans_posi.append(predict)
            if ans == "-1":
                ans_nega.append(predict)
            if predict == "+1":
                predict_posi.append(ans)
            if predict == "-1":
                predict_nega.append(ans)

    accuracy = (predict_posi.count("+1") + predict_nega.count("-1")) / (len(predict_posi) + len(predict_nega))
    precision = predict_posi.count("+1") / len(predict_posi)
    recall = ans_posi.count("+1") / len(ans_posi)
    f1 = (2 * recall * precision) / (recall + precision)
    
    thresholds.append(threshold)
    accuracys.append(accuracy)
    precisions.append(precision)
    recalls.append(recall)
    f1s.append(f1)

def _79():
    for threshold in np.arange(-1, 1, 0.02):
        score(threshold)

    fp = FontProperties(fname="C:\\Windows\\Fonts\\meiryo.ttc")
    
    plt.xlim(xmin=0.5, xmax=1.0)
    plt.ylim(ymin=0, ymax=1.0)
    plt.plot(precisions, recalls)    
    
    plt.xlabel('適合率', fontproperties=fp)
    plt.ylabel('再現率', fontproperties=fp)
    
    plt.legend()


    plt.grid(axis='both')

    plt.show()

    print(precisions)

    print(recalls)
if __name__ == "__main__":
    _79()