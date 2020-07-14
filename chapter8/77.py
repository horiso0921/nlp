def _77():
    predict_posi = []
    predict_nega = []
    ans_posi = []
    ans_nega = []

    with open("76", "r", encoding="latin_1") as target:
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
    _77()

"""
--正解率--
正解率 : 0.8235790658413056

--適合率--
適合率 (肯定) : 0.8195628010374213
適合率 (否定) : 0.8276975683890577

--再現率--
再現率 (肯定) : 0.8298630650909773
再現率 (否定) : 0.8172950665916339

F1値
F1値（肯定）： 0.8246807717401435
F1値（否定）： 0.8224634261444077

"""