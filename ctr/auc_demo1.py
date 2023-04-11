from typing import List


def auc(y_preds, labels):
    if labels is None or len(labels) == 0 or len(labels) != len(y_preds):
        raise Exception("Illigale params")

    all_num = len(labels)
    positive_num = len([1 for i in labels if i == 1])
    negative_num = all_num - positive_num

    temp = zip(y_preds, labels)
    res = sorted(temp, key=lambda kv: kv[0], reverse=False)  # 从小到达排序，升序

    rank_dict = {}
    pred2num = {}
    pred2rank = {}
    new_res = []
    for i, (pred, label) in enumerate(res):
        rank = i + 1
        rank_dict[rank] = (pred, label)
        key = str(pred)
        if pred2num.get(key) is not None:
            pred2num[key] = pred2num.get(key) + 1
            pred2rank[key] = pred2rank.get(key) + rank
        else:
            pred2num[key] = 1
            pred2rank[key] = rank

        if label == 1:
            new_res.append((pred, label))

    psum = 0
    for i, (pred, label) in enumerate(new_res):
        if label == 1:
            key = str(pred)
            new_rank = pred2rank[key]/pred2num[key]
            psum += new_rank

    p1 = psum - positive_num*(positive_num+1)/2
    return p1/(positive_num*negative_num)




if __name__ == '__main__':
    labels = [0, 1, 1, 0, 0, 1, 1, 1]
    preds = [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.8, 0.9]
    res = auc(y_preds=preds, labels=labels)
    print(res)
